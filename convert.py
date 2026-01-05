import pandas as pd
import pyreadstat
import os

import config

# --- 설정 구간 ---
input_file = config.INPUT_FILE       # 변환할 원본 파일명 (같은 폴더에 있어야 함)
output_file = config.OUTPUT_FILE     # 저장될 SPSS 파일명
encoding_type = config.ENCODING_TYPE       # 한글이 깨지면 'cp949'로 변경하세요
# ----------------

def run_convert():
    if not input_file or not str(input_file).strip():
        print("❌ 에러: config.py 파일의 INPUT_FILE 설정값이 비어 있습니다.")
        print("👉 config.py 파일을 열어 원본 파일명을 정확히 입력해 주세요.")
        return

    if not output_file or not str(output_file).strip():
        print("❌ 에러: config.py 파일의 OUTPUT_FILE 설정값이 비어 있습니다.")
        print("👉 config.py 파일을 열어 원본 파일명을 정확히 입력해 주세요.")
        return

    if not encoding_type or not str(encoding_type).strip():
        print("❌ 에러: config.py 파일의 ENCODING_TYPE 설정값이 비어 있습니다.")
        print("👉 config.py 파일을 열어 원본 파일명을 정확히 입력해 주세요.")
        return

    if not os.path.exists(input_file):
        print(f"에러: {input_file} 파일이 현재 폴더에 없습니다.")
        return

    print(f"'{input_file}' 읽는 중...")
	
    
    try:
        # 데이터 읽기 (컬럼이 너무 많아도 파이썬은 잘 읽습니다)
        df = pd.read_csv(input_file, encoding=encoding_type)
        
        print(f"변환 중... (컬럼 수: {len(df.columns)}개)")
        
        # .sav로 저장
        pyreadstat.write_sav(df, output_file)
        
        print(f"성공! '{output_file}' 파일이 생성되었습니다.")
        
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    run_convert()