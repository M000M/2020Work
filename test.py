from multiprocessing import Pool
import requests
def demo(i):
    url="https://vip.okokbo.com/20180114/ArVcZXQd/1000kb/hls/phJ51837151%03d.ts"%i
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36"}
    req=requests.get(url,headers=headers)
    with open('./mp4/ {}'.format(url[-10:]), 'wb') as f:
        f.write(req.content)

if __name__=='__main__':
    pool = Pool(20)
    for i in range(100):
        pool.apply_async(demo, (i,))
    pool.close()
    pool.join()
