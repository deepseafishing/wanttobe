# -*- coding: utf-8 -*-
import ast
import json
import logging
from flask import render_template, request, redirect, url_for, flash, g, session, jsonify
from google.appengine._internal.django.utils.safestring import mark_safe
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import desc
from apps import app, db
from apps.models import People
from apps.forms import JoinForm, LoginForm
import pusher
import copy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# @app.template_filter()
# def json_render(dict):
#
#     return template.render
#


@app.route('/', methods=['GET'])
def start():

    return render_template('index.html',result=json.dumps(make_json()))
#

@app.route('/main', methods=['GET'])
def main():
    return render_template('index2.html')

@app.route('/contents', methods=['GET','POST'])
def contents():
    human1 = People(
        name="임은정",
        exp01="건국대 대학원",
        exp02="성균관대 대학원",
        exp03="한신대 대학원",
        exp04="서울교대 대학원",
        exp05="한국스캐폴딩교육연구소",
        title01="초빙교수",
        title02="겸임교수",
        title03="교육학 석사",
        title04="교육학 박사",
        title05="대표",
        )

    human2 = People(
        name="이영희",
        exp01="연세대",
        exp02="노스웨스턴대 대학원",
        exp03="레오버넷 코리아",
        exp04="유니레버코리아",
        exp05="SC존슨코리아",
        exp06="로레알코리아",
        exp07="삼성전자",
        title01="영문학 학사",
        title02="광고마케팅학 석사",
        title04="마케팅 매니저",
        title05="마케팅 디렉터",
        title06="시판사업부 전무",
        title07="부사장",
    )
    human3 = People(
        name="권계현",
        exp01="연세대",
        exp02="노스웨스턴대 대학원",
        exp03="레오버넷 코리아",
        exp04="유니레버코리아",
        exp05="SC존슨코리아",
        exp06="로레알코리아",
        exp07="삼성전자",
        title01="영문학 학사",
        title02="광고마케팅학 석사",
        title04="마케팅 매니저",
        title05="마케팅 디렉터",
        title06="시판사업부 전무",
        title07="부사장",
    )
    human4 = People(
        name="조현아",
        exp01="코넬대",
        exp02="서던캘리포니아대 대학원",
        exp03="칼호텔네트워크",
        exp04="대한항공",
        title01="호텔경영학 학사",
        title02="경영학 석사",
        title03="대표이사",
        title04="기내서비스,호텔부문 부사장",
    )
    human5 = People(
        name="조성진",
        exp01="용산공업고",
        exp02="LG그룹",
        exp03="부산대 대학원",
        exp04="LG전자",
        title04="최고경영자과정 수료",
        title05="HA사업본부장, 사장",

    )
    human6 = People(
        name="조현민",
        exp01="대한항공",
        exp02="진에어",
        exp03="서울대 대학원",
        exp04="서던캘리포니아대",
        title01="학사",
        title02="글로벌경영학 석",
        title03="등기이사",
        title04="등기이사",
        title05="마케팅본부 전무",
        title06="여객마케팅부 전무",
    )

    human6 = People(
        name="김도현",
        exp01="LG엔시스",
        exp02="LG CNS",
        exp03="LG전자",
        exp04="고려대",

    )



    human7 = People(
        name = "안상수",
        exp01 = "경기고",
        exp02 = "서울대",
        title01 = "학사",
        exp03 = "서울대 대학원",
        title02 = "경영학 석사",
        exp04 = "트로이 대학원",
        title03 = "경영학 석사",
        exp05 = "한국방송통신대",
        title04 = "중어중문학 학사",
        exp06 = "연세대 대학원",
        title05 = "행정학 명예박사",
        exp07 = "동양증권",
        title06 = "이사, 감사, 부사장",
        exp08 = "데이콤",
        title07 = "이사",
        exp09 = "동양그룹",
        title08 = "종합조정실 사장",
        exp10 = "인천광역시",
        title09 = "4대 시장",
        exp11 = "국회",
        title10 = "15대 국회의원",
        exp12 = "국민통합전국시도민연합회",
        title11 = "대표총재",
        exp13 = "새누리당",
        title12 = "재정경제위원장",
    )

    human8 = People(
        name = "허정훈",
        exp01 = "뉴욕공과대학",
        exp02 = "한국수출포장공업",
        title01 = "대표이사",
    )

    human9 = People(
        name = "김영기",
        exp01 = "예산고",
        exp02 = "서강대",
        title01="경제학 학사",
        exp03 = "브리검영대 대학원",
        title02 = "경영학 석사",
        exp04 = "서울과합종합 대학원",
        title03 = "경영학 박사",
        exp05 = "중앙노동위원회",
        title04 = "사용자위원",
        exp06 = "LG전자",
        title05 = "부사장 CRO",
        exp07= "국제백신연구소",
        title06 = "한국후원회 이사"
    )

    human10 = People(
        name = "황영기",
        exp01 = "서울고",
        exp02 = "서울대",
        title01="무역학 학사",
        exp03 = "런던대대학원",
        title02 = "정치경제학 석사",
        exp04 = "삼성물산",
        title03 = "사원",
        exp05 = "뱅커스트러스트은행",
        title04 = "동경지점 국제자본시장부 부사장",
        exp06 = "삼성그룹",
        title05 = "회장비서실 인사팀 팀장",
        exp07= "삼성전자",
        title06 = "자금팀 팀장, 상무",
        exp08 = "삼성생명",
        title07="전략기획실 팀장, 전무",
        exp09 = "한미은행",
        title08 = "비상임이사",
        exp10 = "삼성투자신탁운용",
        title09 = "대표이사",
        exp11 = "재정경제부",
        title10 = "금융발전위원회",
        exp12 = "우리금융지주",
        title11 = "회장",

    )

    human11 = People(
        name="조남성",
        exp01="영훈고",
        exp02="성균관대",
        exp03="카이스트 대학원",
        exp04="삼성 LED",
        exp05="삼성전자",
        exp06="제일모직",
        exp07="삼성SDI",

    )

    human12 = People(
        name="임영록",
        exp01="경기고",
        exp02="서울대",
        exp03="서울대 대학원",
        exp04="밴더빌트대 대학원",
        exp05="한양대 대학원",
        exp06="대통령비서실",
        exp07="재정경제원",
        exp08="경수로사업지원기획단",
        exp09="재정경제부",
        exp10="외교통상부",
        exp11="재정경제부",
        exp12="한국금융연구원",
        exp13="법무법인 충정",
        exp14="KB금융지주",
    )


    human13 = People(
        name = "홍석조",
        exp01 = "경기고",
        exp02 = "서울대",
        title01 = "법학 학사",
        exp03 = "하버드대 대학원",
        title02 = "법학 석사",
        exp04 = "대전지방경찰청",
        title03 = "천안지청 검사",
        exp05 = "서울지방검찰청",
        title04 = "동부지청 검사",
        exp06 = "대검찰청",
        title05 = "기획과장",
        exp07 = "전주지방검찰청",
        title06 = "군사지청 지청장",
        exp08 = "부산지방검찰청",
        title07 = "2차장검사",
        exp09 = "인천지방경찰청",
        title08 = "검사장",
        exp10 = "광주고등검찰청",
        title09 = "검사장",
        exp11 = "보광훼미리맡트",
        title10 = "대표이사",
        exp12 = "BGF리테일",
        title11 = "대표이사",
    )


    human14 = People(
        name = "",
        exp01 = "여의도고",
        exp02 = "서울대",
        title01 = "공법학 학사",
        exp03 = "코넬대 대학원",
        title02 = "법학 석사",
        exp04 = "사법고시",
        title03 = "34회",
        exp05 = "서울지방검찰청",
        title04 = "동부지청 검사",
        exp06 = "통영지방검찰청",
        title05 = "울산지방검찰청",
        exp07 = "인천지방경찰청",
        title06 = "검사",
        exp08 = "대검찰청",
        title07 = "검찰연구관",
        exp09 = "금태섭황선기법률변호사",
        title08 = "변호사",
        exp10 = "법무법인 퍼스트",
        title09 = "파트너변호사",
        exp11 = "법무법인 지평지성",
        title10 = "파트너변호사",
        exp12 = "서강대 대학원",
        title11 = "법학전문 겸임교수",
        exp13 = "법무법인 공존",
        title12 = "변호사",
    )

    human15 = People(
        name = "이현동",
        exp01 = "경북고",
        exp02 = "영남대",
        title01 = "행정학 학사",
        exp03 = "성균관대 대학원",
        title02 = "경영학 석사",
        exp04 = "행정고시",
        title03 = "24회",
        exp05 = "구미세무서",
        title04 = "서장",
        exp06 = "조세심판원",
        title05 = "심판관",
        exp07 = "대구지방경국세청",
        title06 = "조사1국 국장",
        exp08 = "중부지방국세청",
        title07 = "납세자보호담당관",
        exp09 = "서울지방국세청",
        title08 = "청장",
        exp10 = "국세청",
        title09 = "19대 청장",
    )


    human16 = People(
        name = "나경원",
        exp01 = "서울여고",
        exp02 = "서울대",
        title01 = "법학 학사",
        exp03 = "서울대 대학원",
        title02 = "법학 석사, 국제법학 박사수료",
        exp04 = "부산지방법원",
        title03 = "판사",
        exp05 = "인천지방법원",
        title04 = "판사",
        exp06 = "서울행정법원",
        title05 = "판사",
        exp07 = "바른법율",
        title06 = "변호사",
        exp08 = "손기정기념재단",
        title07 = "이사장",
        exp09 = "한나라당",
        title08 = "최고위원",
        exp10 = "사랑나눔",
        title09 = "위캔",
        exp11 = "서울대 대학원",
        title10 = "행정학 초빙교수",
        exp12 = "새누리당",
        title11 = "서울시당위원장",
        exp13 = "국회",
        title12 = "국회의원 17,18,19대",
    )

    human17 = People(
        name = "이상주",

        exp02 = "서울대",
        title01 = "법학 학사",
        exp03 = "조지타운대 대학원",
        title02 = "법학 석사",
        exp04 = "하버드대 대학원",
        title03 = "행정학 석사",
        exp05 = "고려대 대학원",
        title04 = "상법학 박사",
        exp06 = "사법고시",
        title05 = "35회",
        exp07 = "사법연수원",
        title06 = "25기",
        exp08 = "부산지방검찰청",
        title07 = "검사",
        exp09 = "수원지방검찰청",
        title08 = "여주지청 검사",
        exp10 = "삼성화재",
        title09 = "해외법무상무, 준법감시인",
        exp11 = "링클레이터스 법률사무소",
        title10 = "변호사",
        exp12 = "도교대학",
        title11 = "법정대 객원연구원",
        exp13 = "재단법인 청계",
        title12 = "이사",
    )

    human18 = People(
        name = "진현희",
        exp01 = "테레사여고",
        exp02 = "서울대",
        title01 = "치의학 학사",
        exp03 = "고려대 대학원",
        title02 = "의료법학 석사",
        exp04 = "사법고시",
        title03 = "38회",
        exp05 = "대한의료법학회",
        title04 = "상임이사",
        exp06 = "여성연합",
        title05 = "미디어센터 운영위원",
        exp07 = "연세대 대학원",
        title06 = "법의학과 외래부교수",
        exp08 = "대한의사협회",
        title07 = "법제이사",
        exp09 = "대한피부과학회",
        title08 = "고문변호사",
        exp10 = "카톨릭대 대학원",
        title09 = "의료경영대학 외래교수",
        exp11 = "대외법률 연구소",
        title10 = "이사장",
        exp12 = "대한변호사협회",
        title11 = "고문변호사",
        exp13 = "공정거래위원회",
        title12 = "소비자보호실무전문가위원",
        exp14 = "국회",
        title13 ="18대 국회의원"
    )
    db.session.add(human1)
    db.session.add(human2)
    db.session.add(human3)
    db.session.add(human4)
    db.session.add(human5)
    db.session.add(human6)
    db.session.add(human7)
    db.session.add(human8)
    db.session.add(human9)
    db.session.add(human10)
    db.session.add(human11)
    db.session.add(human12)
    db.session.add(human13)
    db.session.add(human14)
    db.session.add(human15)
    db.session.add(human16)
    db.session.add(human17)
    db.session.add(human18)


    db.session.commit()

    return render_template('new.html',result=json.dumps(make_json()))
#result=json.dumps(make_json())

def make_json():
    """
    Jsonify the sql alchemy query result.
    """
    exp=[]
    exps=[]
    ids = People.query.order_by(People.id).all()
    len = People.query.order_by(People.id).count()
    people = People.query.order_by(People.name).all()
    #{source: "우암초등학교", target: "영동중학교", person: "강원준"}
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),default="NULL")
    face = db.Column(db.String(255),default="NULL")
    job_name = db.Column(db.String(255),default="NULL")
    description = db.Column(db.Text(),default="NULL")
    exp01 = db.Column(db.String(255),default="NULL")'''
    if ids:
        for i in ids:
            temp1={}
            temp2={}
            if i.name != "NULL":
                temp1["person"]=i.name
            if i.id != "NULL":
                temp1["id"]= i.id
            if i.face != "NULL":
                temp1["face"]= i.face


            if i.exp02 != "NULL":
                temp2 = copy.deepcopy(temp1)
                temp2["source"] = i.exp01
                temp2["target"] = i.exp02
                temp2["source_info"] = i.title01
                temp2["target_info"] = i.title02
                exps.append(temp2)
                temp2={}


            if i.exp03 != "NULL":
                temp2 = copy.deepcopy(temp1)
                temp2["source"] = i.exp02
                temp2["target"] = i.exp03
                temp2["source_info"] = i.title02
                temp2["target_info"] = i.title03
                exps.append(temp2)
                temp2={}


            if i.exp04 != "NULL":
                temp2 = copy.deepcopy(temp1)
                temp2["source"] = i.exp03
                temp2["target"] = i.exp04
                temp2["source_info"] = i.title03
                temp2["target_info"] = i.title04
                exps.append(temp2)
                temp2={}


            if i.exp05 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp04
                temp2["target"] = i.exp05
                temp2["source_info"] = i.title04
                temp2["target_info"] = i.title05
                exps.append(temp2)
                temp2={}


            if i.exp06 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp05
                temp2["target"] = i.exp06
                temp2["source_info"] = i.title05
                temp2["target_info"] = i.title06
                exps.append(temp2)
                temp2={}


            if i.exp07 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp06
                temp2["target"] = i.exp07
                temp2["source_info"] = i.title06
                temp2["target_info"] = i.title07
                exps.append(temp2)
                temp2={}


            if i.exp08 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp07
                temp2["target"] = i.exp08
                temp2["source_info"] = i.title07
                temp2["target_info"] = i.title08
                exps.append(temp2)
                temp2={}


            if i.exp09 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp08
                temp2["target"] = i.exp09
                temp2["source_info"] = i.title09
                temp2["target_info"] = i.title10
                exps.append(temp2)
                temp2={}


            if i.exp10 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp09
                temp2["target"] = i.exp10
                temp2["source_info"] = i.title09
                temp2["target_info"] = i.title10
                exps.append(temp2)
                temp2={}


            if i.exp11 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp10
                temp2["target"] = i.exp11
                temp2["source_info"] = i.title10
                temp2["target_info"] = i.title11
                exps.append(temp2)
                temp2={}


            if i.exp12 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp11
                temp2["target"] = i.exp12
                temp2["source_info"] = i.title11
                temp2["target_info"] = i.title12
                exps.append(temp2)
                temp2={}


            if i.exp13 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp12
                temp2["target"] = i.exp13
                temp2["source_info"] = i.title12
                temp2["target_info"] = i.title13
                exps.append(temp2)
                temp2={}


            if i.exp14 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp13
                temp2["target"] = i.exp14
                temp2["source_info"] = i.title13
                temp2["target_info"] = i.title14
                exps.append(temp2)
                temp2={}


            if i.exp15 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp14
                temp2["target"] = i.exp15
                temp2["source_info"] = i.title14
                temp2["target_info"] = i.title15
                exps.append(temp2)
                temp2={}


            if i.exp16 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp15
                temp2["target"] = i.exp16
                temp2["source_info"] = i.title15
                temp2["target_info"] = i.title16
                exps.append(temp2)
                temp2={}


            if i.exp17 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp16
                temp2["target"] = i.exp17
                temp2["source_info"] = i.title16
                temp2["target_info"] = i.title17
                exps.append(temp2)
                temp2={}


            if i.exp18 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp17
                temp2["target"] = i.exp18
                temp2["source_info"] = i.title17
                temp2["target_info"] = i.title18
                exps.append(temp2)
                temp2={}


            if i.exp19 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp18
                temp2["target"] = i.exp19
                temp2["source_info"] = i.title18
                temp2["target_info"] = i.title19
                exps.append(temp2)
                temp2={}


            if i.exp20 != "NULL":
                temp2 = temp1
                temp2["source"] = i.exp19
                temp2["target"] = i.exp20
                temp2["source_info"] = i.title19
                temp2["target_info"] = i.title20
                exps.append(temp2)
                temp2={}


        return exps

    else:
        return "error"


