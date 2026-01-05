import pandas as pd
import pyreadstat
import os
import re

def get_config():
    cfg = {}
    config_path = 'config.py'

    if not os.path.exists(config_path):
        return cfg

    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 변수명 = '값' 형태를 찾아내기 위한 정규표현식
        for key in ['INPUT_FILE', 'OUTPUT_FILE', 'ENCODING_TYPE']:
            match = re.search(fr"{key}\s*=\s*['\"](.*?)['\"]", content)
            if match:
                cfg[key] = match.group(1)
    return cfg


def run_convert():
    cfg = get_config()

    input_file = cfg.get('INPUT_FILE', '')
    output_file = cfg.get('OUTPUT_FILE', '')
    encoding_type = cfg.get('ENCODING_TYPE', '')

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
