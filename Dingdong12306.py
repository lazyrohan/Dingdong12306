# -*- coding: utf-8 -*-
"""
by rohan
ver 0.0.1
"""
import time
#import secrets
import io
import requests
from PIL import Image
#Disable security SSL warning
from urllib3 import disable_warnings
from urllib3.exceptions import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)

class Dingdong12306:
    def __init__(self):
        self.session = requests.session()
        self.header = {
                        "Host":"kyfw.12306.cn",
                        "Referer":"https://kyfw.12306.cn/otn/login/init",
                        "Connection":"keep-alive",
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"        
                        }
        
    # 1.Get authurize code
    #Remote Address:113.107.58.182:443
    def captcha(self):
        certUrl = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
        rc = self.session.get(url=certUrl,headers=self.header,verify=False)
        if rc.status_code != 200:
            print(rc.status_code,"connect captcha server failed.")
            print(rc.text)
            self.captcha()
        else:
            #print(rc.content)
            return rc.content
    """
        #show image for certification code
        from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit
        from PyQt5.QtGui import QPixmap
        import sys
        app = QApplication(sys.argv)
        wnd = QWidget()
        wnd.resize(300,300)
        wnd.setWindowTitle("验证码")
        img = QPixmap()
        img.loadFromData(rc.content)
        limg = QLabel(wnd)
        limg.setPixmap(img)
        ltxt = QLabel("Text here",wnd)
        ltxt.move(90,100)
        edit = QLineEdit(wnd)
        edit.move(0,200)
        print(edit.text())
        wnd.show()
        app.exec_()
    """
        
    #2. Post Certification code
    def captchacheck(self,codenum):
        postUrl = "https://kyfw.12306.cn/passport/captcha/captcha-check"
        #post image position(x,y)
        certpos = ["53,37","113,37","193,36","237,37","33,113","121,111","205,112","247,111"]
        certnums = []
        # Get input
        #codenum = input("请输入识别的验证码图片编号,0-7: ")
        # translate input num to image coordinates
        for num in codenum:
            certnums.append(certpos[int(num)])    
        postData = {"answer":certnums,"login_site":"E","rand":"sjrand"}
        rp = self.session.post(url=postUrl,data=postData,headers=self.header,verify=False)
        return rp.json()["result_message"]
           
    ##############3. uamtk##################
    def uamtk(self):
        uamtk = "https://kyfw.12306.cn/passport/web/auth/uamtk"
        udata = {"appid":"otn"}
        ru = self.session.post(uamtk,headers=self.header,data=udata,verify=False)
        print(ru.json())#["result_message"])
        return ru.json()  
    
    #4. Post account info
    #######3. Login function################################################
    def loginto(self):
        #1) login to init page
        loginit = "https://kyfw.12306.cn/otn/login/init"
        self.session.get(loginit,headers=self.header,verify=False)
        
        #) check logined
        loginstatus = self.uamtk()
        print(loginstatus)
        if loginstatus["result_code"] == 1:
            #2) certification code check
           self.captcha()
           usr = "rohanr"#input("用户名: ")
           psw = "alin520526"#input("密码: ")
           loginurl ="https://kyfw.12306.cn/passport/web/login"
           logindata={"username":usr,"password":psw,"appid":"otn"}
           rl = self.session.post(url=loginurl,headers=self.header,data=logindata,verify=False)
           #{"result_message":"登录成功","result_code":0,"uamtk":"FX4aNxll3XLCHe_XVUuIne5aVfPdmBIZxhr1r0"}
           rcontype = rl.headers.get("Content-Type")
           if rcontype == "application/json;charset=UTF-8":
              print(rl.json()["result_message"])
              return rl.json()
           else:
              print(rcontype,"登陆失败,重新登陆")
              if rl.encoding != "utf-8":
                  rl.encoding = "utf-8"
                  print(rl.text)
              rl.cookies.clear()
              self.loginto()
    
    #######4. uamtkclient#############################################################
    def uamtkclient(self,uamtk):
        uclient = "https://kyfw.12306.cn/otn/uamauthclient"
        ucdata = {"tk":uamtk}
        ruc = self.session.post(url=uclient,headers=self.header,data=ucdata,verify=False)
        print(ruc.text)
        return ruc.json()
    
    #######5. queryticket#######################################################
    def queryticket(self):
        queryTicketRoot = "https://kyfw.12306.cn/otn/leftTicket/queryZ"
        traindate = "2018-02-15"#time.strftime('%Y-%m-%d',time.localtime(time.time()))
        fromstation = "SZQ"
        tostation = "WXN"
        ticketPam = {"leftTicketDTO.train_date":traindate,
                     "leftTicketDTO.from_station":fromstation,
                     "leftTicketDTO.to_station":tostation,
                     "purpose_codes":"ADULT"
                     }
        rqt = self.session.get(queryTicketRoot,params=ticketPam,headers=self.header,verify=False)
        #print(rqt.text)
        ticketinfos = rqt.json()["data"]["result"]
        secretStr = ""
        for info in ticketinfos:
            ticketInfo = info.split("|")
            #print(ticketInfo)
            secretHBStr = ticketInfo[36];
            secretStr = ticketInfo[0]
            buttonTextInfo = ticketInfo[1];
            train_no = ticketInfo[2];
            #车次
            station_train_code = ticketInfo[3];
            start_station_telecode = ticketInfo[4];
            end_station_telecode = ticketInfo[5];
            from_station_telecode = ticketInfo[6];
            to_station_telecode = ticketInfo[7];
            #始发时间
            start_time = ticketInfo[8];
            arrive_time = ticketInfo[9];
            lishi = ticketInfo[10];
            canWebBuy = ticketInfo[11];
            #余票信息?
            yp_info = ticketInfo[12];
            start_train_date = ticketInfo[13];
            train_seat_feature = ticketInfo[14];
            location_code = ticketInfo[15];
            from_station_no = ticketInfo[16];
            to_station_no = ticketInfo[17];
            is_support_card = ticketInfo[18];
            controlled_train_flag = ticketInfo[19];
            gg_num = ticketInfo[20]
            gr_num = ticketInfo[21]
            qt_num = ticketInfo[22]
            #软卧
            rw_num = ticketInfo[23]
            rz_num = ticketInfo[24]
            tz_num = ticketInfo[25]
            #无座
            wz_num = ticketInfo[26]
            yb_num = ticketInfo[27]
            #硬卧
            yw_num = ticketInfo[28]
            #硬座
            yz_num = ticketInfo[29]
            ze_num = ticketInfo[30]
            zy_num = ticketInfo[31]
            swz_num = ticketInfo[32]
            rrb_num = ticketInfo[33]
            yp_ex = ticketInfo[34]
            seat_types = ticketInfo[35]
            print(station_train_code,"始发时间:",start_train_date,start_time,"硬座:",yz_num,"硬卧:",yw_num)
        if  secretStr != "":
            print("有票")
            return secretStr,yp_info
        else:
            print(time.strftime('%H:%M:%S',time.localtime(time.time())),"无票")
            time.sleep(0.1)
            self.queryticket()
            
    #########GetPasssengerInfo##################################################    
    def getpassengerinfo(self):
        getpsgurl ="https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"    
        psgdata = {"REPEAT_SUBMIT_TOKEN":"c412871cf1417f65f9e1f2c73b52d71d"}
        rpsg = self.session.post(getpsgurl,headers=self.header,data=psgdata,verify=False)
        print(rpsg.text)
        
    ##################checkuser################################################
    def checkuser(self):
        checkusrurl = "https://kyfw.12306.cn/otn/login/checkUser"
        rcu = self.session.post(checkusrurl,headers=self.header,verify=False)
        print(rcu.text)
        return rcu.json()["data"]["flag"]
        
    ############submitorderrequest#################################################
    def submitorderrequest(self):
        suborderurl = "https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
        subdata = {
                  "secretStr":"BWrC4LCammzezl3prL0K/4maDENFl+1ibz3ngJ74mP4NgMaP+K8Xsk6mPpp1NVzl1M0YOoi3Xnon",
                  "train_date":"2018-02-14",
                  "back_train_date":"2018-01-16",
                  "tour_flag":"dc",
                  "purpose_codes":"ADULT",
                  "query_from_station_name":"深圳",
                  "query_to_station_name":"武穴",
                  "undefined":""
                  }
        rsub = self.session.post(suborderurl,headers=self.header,data=subdata,verify=False)
        print(rsub.text)
    ##########checkorderinfo#####################################
    def checkorderinfo(self):
        checkorderurl = "https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
        checkdata = {
                     "cancel_flag":2,
                     "bed_level_order_num":"000000000000000000000000000000",
                     "passengerTicketStr":"1%2C0%2C1%2C%E9%98%AE%E7%81%BF%E5%BB%BA%2C1%2C421182198309214177%2C15818575246%2CN",
                     "oldPassengerStr":"%E9%98%AE%E7%81%BF%E5%BB%BA%2C1%2C421182198309214177%2C1_",
                     "tour_flag":"dc",
                     "randCode":"",
                     "whatsSelect":1,
                     "REPEAT_SUBMIT_TOKEN":"c412871cf1417f65f9e1f2c73b52d71d"
                    }
        rcheck = self.session.post(checkorderurl,headers=self.header,data=checkdata,verify=False)
        print(rcheck.text)
    
    #########getQueueCount#############
    def getqueuecount(self):
        getqueurl = "https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount"
        quedata = {
                   "train_date":"Thu+Feb+15+2018+00%3A00%3A00+GMT%2B0800+(China+Standard+Time)",
                   "train_no":"650000K82402",
                   "stationTrainCode":"K824",
                   "seatType":1,
                   "fromStationTelecode":"BJQ",
                   "toStationTelecode":"WXN",
                   "leftTicket":"5G1YAQoXFCB063z0qu7F8WYFK4OiLgTK8S4IZXiyeejNJukvHZ%2FHvtmO%2BH8%3D",
                   "purpose_codes":"00",
                   "train_location":"Q7",
                   "_json_att":"",
                   "REPEAT_SUBMIT_TOKEN":"c412871cf1417f65f9e1f2c73b52d71d"
                }
        rq = self.session.post(getqueurl,headers=self.header,data=quedata,verify=False)
        print(rq.text)
        
    ##########confirmSingleForQueue#######################
    def confirmsingleforqueue(self):
        confurl = "https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
        condata = {
                   "passengerTicketStr":"1,0,1,阮灿建,1,421182198309214177,15818575246,N",
                   "oldPassengerStr":"阮灿建,1,421182198309214177,1_",
                   "randCode":"",
                   "purpose_codes":"00",
                   "key_check_isChange":"9EFBA275BC092DDC2C058DCCAF680A7A6D8A463718E8BD571AB5F0C3",
                   "leftTicketStr":"5G1YAQoXFCB063z0qu7F8WYFK4OiLgTK8S4IZXiyeejNJukvHZ%2FHvtmO%2BH8%3D",
                   "train_location":"Q7",
                   "choose_seats":"",
                   "seatDetailType":"000",
                   "whatsSelect":1,
                   "roomType":"00",
                   "dwAll":"N",
                   "REPEAT_SUBMIT_TOKEN":"c412871cf1417f65f9e1f2c73b52d71d"
                  }
        rcon = self.session.post(confurl,headers=self.header,data=condata,verify=False)
        print(rcon.text)
        
    ###########queryOrderWaitTime#################################
    def queryorderwaittime(self):
        qurl = "https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime"
        param ={
                "random":"1516086113921",
                "tourFlag":"dc",
                "_json_att":"",
                "REPEAT_SUBMIT_TOKEN":"c412871cf1417f65f9e1f2c73b52d71d"
                }
        rq = self.session.get(qurl,headers=self.header,params=param,verify=False)
        print(rq.text)
        
    #############resultOrderForDcQueue########################
    def resultorderforqueue(self):
        rurl = "https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"
        rdata = {
                "orderSequence_no":"EA39818077",
                "_json_att":"",
                "REPEAT_SUBMIT_TOKEN":"c412871cf1417f65f9e1f2c73b52d71d"
                } 
        rr = self.session.post(rurl,headers=self.header,data=rdata,verify=False)
        print(rr.text)
    
#resultl = loginto(se,header)
#uamtk(se,header)
#queryticket(se,header)
#getpassengerinfo(se,header)
#checkuser(se,header)
#submitorderrequest(se,header)
#checkorderinfo(se,header)
#getqueuecount(se,header)
#confirmsingleforqueue(se,header)
#queryorderwaittime(se,header)
#resultorderforqueue(se,header)