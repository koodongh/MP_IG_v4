import requests
import time
import os
import sys
import shutil
def removeAllFile(root):
    if os.path.exists(root):
        for file in os.scandir(root):
            shutil.rmtree(file.path)
        return ('All Remove')
    else:
        return print('No File')

def restart():
    os.execl(sys.executable, sys.executable,*sys.argv)

def run(code):

    while True:
        start_time = time.time()  # 시작 시간 저장
        t = '/home/user/_SEND/'
        #t1 = t + str(start_time) + '.jpg'
        t1 = t + 'abc.jpg'
        # 업로드할 이미지 파일 경로
        image_file_path = '/home/user/_SEND/M'+str(code)+'.jpg'  # 실제 파일 경로로변경해야 합니다.


        # 업로드할 URL (메인 컴퓨터의 Flask API 엔드포인트)
        upload_url = 'http://202.31.101.250:' +str(code)+'/upload'  # 메인 컴퓨터의 IP 주소로 변경해야 합니다.

        if os.path.exists(image_file_path):
            print('Permission Check : ======== ',os.access(image_file_path,os.F_OK))
            if os.access(image_file_path,os.F_OK) == False:
                time.sleep(0.5)

            #shutil.copy(image_file_path,t1)
            pre_size = os.path.getsize(image_file_path)
            time.sleep(0.1)
            post_size = os.path.getsize(image_file_path)

            if pre_size == post_size:
                #time.sleep(0.1)
                # 이미지 업로드
                print(post_size, pre_size)
                files = {'file': open(image_file_path, 'rb')}
                print('upload start')
                #print(t1)
                response = requests.post(upload_url, files=files)


                # 업로드 결과 확인
                if response.status_code == 200:
                    res_data = response.json()
                    print('Result', res_data.get('message', ''))
                    if res_data['message'] == 'IG':
                        r_ = '/home/user/IG_'
                        if os.path.exists(r_):
                            pass
                        else:
                            os.mkdir(r_)
                        r = '/home/user/IG_/log.txt'
                        with open(r,'w') as f:
                            f.write('----NONE' + '/n')
                        f.close()

                    else:
                        print('PASS')
                    #print('File uploaded and processed successfully')
                else:
                    print('Error:', response.json())

                end_time = time.time()  # 종료 시간 저장

                print(f"코드 실행 시간: {end_time - start_time} 초")
                os.remove(image_file_path)
                os.system('sudo apt-get clean')
                return
                #os.system('sudo echo 3 > /proc/sys/vm/drop_caches')

if __name__ == "__main__":
    try:
        #code = 2901
        run(code)
    except Exception as e:
        print('ERROR ====' ,e)
        time.sleep(0.1)
