#pip install gspread
#pip install --upgrade oauth2client


#라이브러리 불러오기
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#구글 시트 API 정보 입력하기
scope = ['https://spreadsheets.google.com/feeds']
json_file_name = '/Users/mac_yk/OneDrive/@coding/hanbit_crawling/hbprojectyk-5c5f3b0ec892.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1gqL7yS5xS-ER2Nyp9hxA9_63GOM8I0Qy_8x0Xh7eUmA/edit?usp=sharing'

#문서 및 시트 불러오기
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('a')

##읽기
#셀읽기
cell_data = worksheet.acell('B2').value
#행읽기
row_data = worksheet.row_values(2)
#열읽기
column_data = worksheet.col_values(1)
#범위 읽기
range_list = worksheet.range('A1:D3')
for cell in range_list:
    print(cell.value)


##쓰기
#셀 업데이트
worksheet.update_acell('B1', 'b1 updated')

#행 추가하기
#원본 링크에서는 맨 아래쪽에 줄이 추가되나 따라 하였을 경우 데이터가 마지막으로 존재하는 행 이후에 작성
worksheet.append_row(['new1', 'new2', 'new3', 'new4'])

#특정 행 추가
worksheet.insert_row(['new1', 'new2', 'new3', 'new4'], 5)

#시트 크기 맞추기
worksheet.resize(20,10)