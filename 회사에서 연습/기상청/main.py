from flask import Flask, make_response, render_template, request, send_file
from flask_cors import CORS
import os
import glob
from configure import *
from io import StringIO, BytesIO
import csv

app = Flask(__name__)

@app.route(prefix + '/')
def res():
    return render_template('index.html')

# @app.route(prefix + '/getTableData')
@app.route(prefix + '/getGridData')
def getTableData():
    targetTime = request.args.get('time')
    try:

        table_files = glob.glob(os.path.join(data_dir, 'CCTM_POST_v54_gcc_NONSAN_*_li.csv'))
        grid_files = glob.glob(os.path.join(data_dir, 'CCTM_POST_v54_gcc_NONSAN_*_grid.csv'))
        # 파일명에 시간 들어갈때
        # table_dates = {os.path.basename(f)[11:26] for f in table_files}
        # grid_dates = {os.path.basename(f)[13:28] for f in grid_files}
        # 파일명에 시간 안들어갈때
        table_dates = {os.path.basename(f).split('_')[5] for f in table_files}
        grid_dates = {os.path.basename(f).split('_')[5] for f in grid_files}

        common_dates = sorted(table_dates & grid_dates, reverse=True)
        previous_dates = [date for date in common_dates if date <= targetTime]
        if previous_dates:  
            latest_date = previous_dates[0]
            table_file = os.path.join(data_dir, f'CCTM_POST_v54_gcc_NONSAN_{latest_date}_li.csv')
            grid_file = os.path.join(data_dir, f'CCTM_POST_v54_gcc_NONSAN_{latest_date}_grid.csv')
            
            # response = make_response(send_file(table_file, as_attachment=True))
            response = make_response(send_file(grid_file, as_attachment=True))
            response.headers['File-Name'] = os.path.basename(table_file)
            response.headers['Grid-File-Name'] = os.path.basename(grid_file)
            response.headers['File-Date'] = latest_date
            return response
        else:
            
            return "No CSV files available", 404
    except Exception as e:
        print(e) 
        return make_response(f"Error : {str(e)}",500)
    
# @app.route(prefix + '/getGridData')
@app.route(prefix + '/getTableData')
def getGridData():
    targetTime = request.args.get('time')
    try:
        # grid_file = os.path.join(data_dir, f'ALL_grid_48h_{targetTime}.csv')
        grid_file = os.path.join(data_dir, f'CCTM_POST_v54_gcc_NONSAN_{targetTime}_li.csv')
        response = make_response(send_file(grid_file, as_attachment=True))
        response.headers['File-Name'] = os.path.basename(grid_file)
        response.headers['File-Date'] = targetTime
        return response
        
    except Exception as e:
        print(e)
        return make_response(f"Error : {str(e)}",500)
    
@app.route(prefix + '/getMasking')
def getMasking():
    try:
        # grid_file = os.path.join(data_dir, f'ALL_grid_48h_{targetTime}.csv')
        grid_file = os.path.join(masking_dir, f'masking.csv')
        response = make_response(send_file(grid_file, as_attachment=True))
        return response
        
    except Exception as e:
        print(e)
        return make_response(f"Error : {str(e)}",500)

@app.route(prefix + '/download')
def download():
    type = request.args.get('type')
    targetTime = request.args.get('time')
    
    try:
        path = os.path.join(data_dir, f'CCTM_POST_v54_gcc_NONSAN_{targetTime}_li.csv')
        
        if not os.path.exists(path):
            return "File not found", 404
        
        output = StringIO()
        writer = csv.writer(output)
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # CSV 파일의 헤더를 읽어옵니다.
            filtered_header = ['날짜', '시각', '읍면동', '법정리', '대기오염 영향지수', '악취 영향지수']
            writer.writerow(filtered_header)
            # writer.writerow(header)  # 헤더를 출력 파일에 씁니다.
            
            for row in reader:
                if type == 'GY':
                    if row[2] in ['연무읍', '광석면']:  # EMD_KOR_NM 컬럼이 '연무읍'이나 '광석면'인지 확인
                        filtered_row = row[:4] + row[5:]
                        filtered_row[1] = "%02d" % (int(row[1]) // 10000)
                        filtered_row[4] = {'1': '좋음', '2': '보통', '3': '나쁨', '4': '매우 나쁨'}.get(filtered_row[4], '')
                        filtered_row[5] = {'1': '좋음', '2': '보통', '3': '나쁨', '4': '매우 나쁨'}.get(filtered_row[5], '')
                        writer.writerow(filtered_row)
                else:
                    filtered_row = row[:4] + row[5:]
                    filtered_row[1] = "%02d" % (int(row[1]) // 10000)
                    filtered_row[4] = {'1': '좋음', '2': '보통', '3': '나쁨', '4': '매우 나쁨'}.get(filtered_row[4], '')
                    filtered_row[5] = {'1': '좋음', '2': '보통', '3': '나쁨', '4': '매우 나쁨'}.get(filtered_row[5], '')
                    writer.writerow(filtered_row)
            
        # 필터링된 데이터를 메모리에 저장합니다.
        output.seek(0)
        buffer = BytesIO()
        buffer.write(output.getvalue().encode('utf-8'))
        # buffer.write(output.getvalue().encode('ANSI')) # Excel 용으로는 이 인코딩 사용 권장
        buffer.seek(0)
        
        # 필터링된 데이터를 클라이언트에게 전송합니다.
        return send_file(buffer, as_attachment=True, download_name=f'li_{targetTime}.csv', mimetype='text/csv')
    
    except Exception as e:
        print(e)
        return make_response(f"Error: {str(e)}", 500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = serverPort)