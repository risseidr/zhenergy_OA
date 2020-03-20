#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
from time import sleep

import win32gui

import urllib.parse


def main():
    a = '''
    <div class="row-container" style="padding:0 20px">

    <table class="table table-striped  table-bordered" width="100%" border="1">
    <tbody><tr valign="top"><td style="width:130px" width="10%" valign="middle"><div align="center"><b> </b><font color="#808080">发件人：</font></div></td><td width="90%" valign="middle"><font color="#00A000">荣伟</font><font color="#808080">/设备管理部/浙能台二</font><font color="#808080">    [时间：</font><font color="#808080">2020-03-18 15:45:30</font><font color="#808080">]</font></td></tr>

    <tr valign="top"><td width="10%" valign="middle"><div align="center"><b> </b><font color="#808080">收件人：</font></div></td><td width="90%" valign="middle"><div id="SendTodiv" style="height:100%;overflow:auto"> 朱彬源 <font color="#818181">&lt;U14411/zhenergy@zhenergy&gt;</font>, 杨景焜 <font color="#818181">&lt;U15422/zhenergy@zhenergy&gt; </font></div></td></tr>

    <tr valign="top"><td style="border-bottom:1 solid #CBCCD0" width="10%" valign="middle"><div align="center"><font color="#808080">主　题：</font></div></td><td width="90%" valign="middle"><b>转发: 转发: 2003-2019年度科技项汇总表，表格请于3月25日前（下周三）反馈给黄路遥。请各主管务必于下周二前汇总反馈给奚彩霞。</b> </td></tr>

    <tr valign="top"><td class="text-center" style="vertical-align: middle;" width="10%">附&nbsp;&nbsp;&nbsp;件：</td><td width="90%"><div>
    <div class="fileOne"><input type="checkbox" name="fj" class="fj" value="2003-2019%E5%B9%B4%E5%BA%A6%E7%A7%91%E6%8A%80%E9%A1%B9%E6%B1%87%E6%80%BB%E8%A1%A8.xlsx"><span class="fileExt xlsx"><a href="javascript:getFile('2003-2019年度科技项汇总表.xlsx')">2003-2019年度科技项汇总表.xlsx</a></span></div> <div class="fileOne"><input type="checkbox" name="fj" class="fj" value="%E9%97%AE%E9%A2%98%E6%B1%87%E6%80%BB%E8%A1%A8.xls"><span class="fileExt xls"><a href="javascript:getFile('问题汇总表.xls')">问题汇总表.xls</a></span></div>
    </div>
    <div style="width:250px;padding-top:10px">
    <a href="#" id="df" class="btn btn-sm btn-default" onclick="downloadSelected()" style="display:none">下载选中附件</a>	
    	<a href="#" id="dfAll" style="display:none" class="btn btn-sm btn-default" onclick="downloadAll();">下载所有附件</a>
    </div>
    <div style="float: left; min-width: 650px; height: 1px; line-height: 1px; background: rgb(255, 255, 255); margin-top: 10px; margin-bottom: 5px; position: fixed; bottom: 0px;" id="ocxDiv"><object id="TANGER_OCX" clsid="{E8FD8E76-203A-48ed-9C39-481479080C34}" foronfileselecteded="FileSelecteded" foronlocalfileadded="OnLocalFileAdded" foronbeforefileadded="BeforeFileAdded" foronaftersavetourl="AfterSaveToURL" foronafterfiledeleted="AfterFileDeleted" _productcaption="浙江省能源集团有限公司" _productkey="681C6D0EC532603F9A6720F884139D54D7D2CC44" codebase="/static_new/ntko/filecontrol/ntkofman.cab#version=5,1,1,8" width="1px" height="1px" type="application/ntko-plug" _noexpirekey="24D07CBB19C267EC7D56A9DFD49B73DF" _isuseutf8url="-1" _isuseutf8data="-1" _borderstyle="1" _bordercolor="ffffff" _menubarcolor="14402205" _menubuttoncolor="16180947" _menubarstyle="3" _isshowcolumnheader="false" viewtype="2" _toolbar="0" _statusbar="0" _isconfirmsavemodified="false" _isshowcontextmenu="false" _isneedsavetoserver="true" _isconfirmdelfiles="false" _"backcolor="16513011" _menubuttonstyle="7" _webusername="NTKO" _caption="NTKO OFFICE文档控件示例演示 http://www.ntko.com">    <span style="color:red">尚未安装NTKO Web Chrome跨浏览器插件。请点击<a href="/static_new/ntko/setup.exe">安装组件</a></span>   </object></div>
    </td></tr>
    </tbody></table>
    <div id="divLinks" style="border:solid blue;visibility:hidden"><a onclick="javascript:return false" href="/mail/znte/U14411.nsf/0/98E01A53C7928E2D4825852F002A9ADE/$file/2003-2019年度科技项汇总表.xlsx">2003-2019年度科技项汇总表.xlsx</a><br><a onclick="javascript:return false" href="/mail/znte/U14411.nsf/0/98E01A53C7928E2D4825852F002A9ADE/$file/问题汇总表.xls">问题汇总表.xls</a><br></div>
    <div id="MailBody" style="display:none">
    <br>
    ------------------ 原始邮件 ------------------<br>
    发件人: 王焕明<br>
    发送时间:2020/3/18 14:33:10<br>
    收件人:卢敏亚,龙伟军,傅林平,屠海彪,李春富,钟金辉,方匡坤,陈胡敏,荣伟,余绍斌,李文杰,邵铃敏,姚凯,奚彩霞<br>
    主题: 转发: 2003-2019年度科技项汇总表，表格请于3月25日前（下周三）反馈给黄路遥。请各主管务必于下周二前汇总反馈给奚彩霞。<br>
    <br>
    <br>
    <br>
    <br>
    <br>
    ------------------ 原始邮件 ------------------<br>
    发件人: 黄路遥<br>
    发送时间: 2020/3/18 14:26:02<br>
    收件人:沈红昌 ,林彤 ,李森明 ,王焕明 ,杨洪涛 ,陈章伟 ,鲍丽娟 ,董宇鸣 ,洪雷 ,王杰 ,程声樱 ,谢增孝 ,曹阳 ,周方盛 ,高军 ,徐新果 ,潘世汉 ,朱新平 <br>
    主题: 2003-2019年度科技项汇总表 <br>
    <br>
    <br>
    为进一步优化科技项目过程管理，提高实施效率，真正发挥科技创新助力安全生产这一作用，现组织各单位对目前科技管理中存在的问题（尤其是 项目在采购过程中存在的困难）进行 梳理。同时为了有效促进优质科技成果推广或转化，拟组织对近6年已完成的科技项目成果进行收集。请各单位务必重视，谢谢。<br>
    。<br>
    ------------------<br>
    黄路遥<br>
    浙江浙能电力股份有限公司 生产安全部<br>
    办公室电话： 0571-86669171<br>
    手机：13868772888（600）<br>
    公司地址：杭州市天目山路152号浙能大厦808室 
    </div>
    <div id="divBody" style="font-size:16px">
    <br><br><br>------------------ 原始邮件 ------------------<div style="background: rgb(239, 239, 239); padding: 8px; font-size: 12px;"><b>发件人: </b>王焕明<br><b>发送时间:</b>2020/3/18 14:33:10<br><b>收件人:</b>卢敏亚<u07227 zhenergy@zhenergy="">,龙伟军<u07228 zhenergy@zhenergy="">,傅林平<u07233 zhenergy@zhenergy="">,屠海彪<u07202 zhenergy@zhenergy="">,李春富<u07231 zhenergy@zhenergy="">,钟金辉<u07229 zhenergy@zhenergy="">,方匡坤<u07241 zhenergy@zhenergy="">,陈胡敏<u07239 zhenergy@zhenergy="">,荣伟<u07244 zhenergy@zhenergy="">,余绍斌<u07212 zhenergy@zhenergy="">,李文杰<u13404 zhenergy@zhenergy="">,邵铃敏<u04576 zhenergy@zhenergy="">,姚凯<u14302 zhenergy="">,奚彩霞<u11469 zhenergy=""><br><b>主题: </b>转发: 2003-2019年度科技项汇总表，表格请于3月25日前（下周三）反馈给黄路遥。请各主管务必于下周二前汇总反馈给奚彩霞。</u11469></u14302></u04576></u13404></u07212></u07244></u07239></u07241></u07229></u07231></u07202></u07233></u07228></u07227></div><br><br><br><br><br>------------------ 原始邮件 ------------------<div style="background: rgb(239, 239, 239); padding: 8px; font-size: 12px;"><b>发件人: </b>黄路遥<br><b>发送时间:
    </b>2020/3/18 14:26:02<br><b>收件人:</b>沈红昌 <u01380 zhenergy@zhenergy="">,林彤 
    <u02133 zhenergy@zhenergy="">,李森明 <u08545 zhenergy@zhenergy="">,王焕明 <u07226 zhenergy@zhenergy="">,杨洪涛 <u04238 zhenergy@zhenergy="">,陈章伟 <u05536 zhenergy="">,鲍丽娟 <u04803 zhenergy="">,董宇鸣 <u00501 zhenergy="">,洪雷 <u06063 zhenergy="">,王杰 <u01797 zhenergy="">,程声樱 <u04067 zhenergy="">,谢增孝 <u09311 zhenergy="">,曹阳 <u01525 zhenergy="">,周方盛 <u01620 zhenergy="">,高军 <u07027 zhenergy="">,徐新果 <u01169 zhenergy="">,潘世汉 <u04036 zhenergy="">,朱新平 <u00227 zhenergy=""><br><b>主题: </b>2003-2019年度科技项汇总表
    </u00227></u04036></u01169></u07027></u01620></u01525></u09311></u04067></u01797></u06063></u00501></u04803></u05536></u04238></u07226></u08545></u02133></u01380></div><br><br>为进一步优化科技项目过程管理，提高实施效率，真正发挥科技创新助力安全生产这一作用，现组织各单位对目前科技管理中存在的问题（尤其是
    项目在采购过程中存在的困难）进行
    梳理。同时为了有效促进优质科技成果推广或转化，拟组织对近6年已完成的科技项目成果进行收集。请各单位务必重视，谢谢。<br>。<br><span id="signloc">------------------<br>黄路遥<br>浙江浙能电力股份有限公司 生产安全部<br>办公室电话： 
    0571-86669171<br>手机：13868772888（600）<br>公司地址：杭州市天目山路152号浙能大厦808室</span>

    </div>
    <iframe id="IFBody" style="WIDTH:100%;display:none;overflow:visible" scrolling="auto"></iframe>
    </div>
    '''

    # print(a)

    for i in re.findall(r'"javascript:getFile\(.*?\)">', a):
        print(i)


if __name__ == '__main__':
    main()
