# -*- coding: utf-8 -*-

import data_values
import f
import random
import datetime
import time

# 住院
dataCount = 1000  #1k
def genDataBase(fileName, dataCount):
    outp = open(fileName, 'w',encoding='utf-8')
    i = 0
    while i < dataCount:
        people_item = f.genRandomTypes(data_values.people_list)
        doctor_name = f.genRandomTypes(data_values.name_list)

        id = f.genPK(19)
        record_no = people_item['record_id']
        name = people_item['name']




        resident_name =name
        gmt_interview =f.genRandomDay()
        symptom_code =f.genRandomString(10)
        symptom_desc =f.genRandomString(10)
        interview_way =f.genRandomString(10)
        interview_way_desc =f.genInt(4)
        l_sbp =f.genRandomString(10)
        l_dbp =f.genRandomString(10)
        r_sbp =f.genRandomString(10)
        r_dbp =f.genRandomString(10)
        weight =f.genRandomString(10)
        bmi =f.genRandomString(10)
        heart_rate =f.genInt(100,60)
        physical_other =f.genRandomString(10)
        daily_smoke_amount =f.genRandomString(1)
        daily_drink_amount =f.genRandomString(1)
        sport_frequency =f.genRandomString(10)
        sport_duration_per =f.genRandomString(3)
        mind_status =f.genRandomString(10)
        mind_desc =f.genRandomString(10)
        salt_intake_status =f.genRandomString(10)
        auxiliary_other =f.genRandomString(10)
        obey_status =f.genRandomString(10)
        obey_status2 =f.genRandomString(10)
        dar_code =f.genRandomString(10)
        drug_dependence_code =f.genRandomString(10)
        drug_dependence_desc =f.genRandomString(10)
        dar_desc =f.genRandomString(10)
        classification_code =f.genRandomString(1)
        classification_desc =f.genRandomString(10)
        drug_name1 =f.genRandomString(10)
        drug_way1 =f.genRandomString(10)
        drug_dose1 =f.genRandomString(10)
        drug_name2 =f.genRandomString(10)
        drug_way2 =f.genRandomString(10)
        drug_dose2 =f.genRandomString(10)
        drug_name3 =f.genRandomString(10)
        drug_way3 =f.genRandomString(10)
        drug_dose3 =f.genRandomString(10)
        other_drug_name =f.genRandomString(10)
        other_drug_way =f.genRandomString(10)
        other_drug_dose =f.genRandomString(10)
        tt_code =f.genInt(3,1)
        tt_reason =f.genRandomString(10)
        tt_org_name =data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        tt_department_name =data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        doctor_id =f.genRandomString(19)
        doctor_name =data_values.name_list[f.genInt(len(data_values.name_list))]
        org_id =f.genRandomString(10)
        org_name = data_values.hospital_list[f.genInt(len(data_values.hospital_list))][1]
        gmt_next =f.genDateList()[2]
        create_time =f.createTime()
        update_time =f.createTime()
        status = 0

        mLine = " %s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s\n" % (
            id,
            record_no,
            resident_name,
            gmt_interview,
            symptom_code,
            symptom_desc,
            interview_way,
            interview_way_desc,
            l_sbp,
            l_dbp,
            r_sbp,
            r_dbp,
            weight,
            bmi,
            heart_rate,
            physical_other,
            daily_smoke_amount,
            daily_drink_amount,
            sport_frequency,
            sport_duration_per,
            mind_status,
            mind_desc,
            salt_intake_status,
            auxiliary_other,
            obey_status,
            obey_status2,
            dar_code,
            drug_dependence_code,
            drug_dependence_desc,
            dar_desc,
            classification_code,
            classification_desc,
            drug_name1,
            drug_way1,
            drug_dose1,
            drug_name2,
            drug_way2,
            drug_dose2,
            drug_name3,
            drug_way3,
            drug_dose3,
            other_drug_name,
            other_drug_way,
            other_drug_dose,
            tt_code,
            tt_reason,
            tt_org_name,
            tt_department_name,
            doctor_id,
            doctor_name,
            org_id,
            org_name,
            gmt_next,
            create_time,
            update_time,
            status
        )

        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase('.\\data\\tbl_hypertension_interview.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end - start))
    print('Ok')
