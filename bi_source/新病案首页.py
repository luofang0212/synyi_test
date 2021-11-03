#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_bi import PlSqlDbBI
from util.dbPlsql_util_system import PlSqlDb
import random
from datetime import datetime, timedelta
from bi_source.get_data import GetData

mysql_bi = PlSqlDbBI()
sql_1 = '''select max(case_id) from source.new_case_base;'''
res_1 = mysql_bi.query(sql_1)

max_case_id = res_1[0][0] + 1
# max_case_id =  1
mysql_2 = PlSqlDb()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''
res_2 = mysql_2.query(sql_2)
# print(len(res_2))

drgs_sql = '''select in_diag_name,in_diag_code  from source.case_base where in_diag_name is not null  group by in_diag_name,in_diag_code;'''
drgs_data = mysql_bi.query(drgs_sql)
print(len(drgs_data))

for i in range(1, 1209):
    max_case_id = max_case_id + 1
    res_2 = mysql_2.query(sql_2)

    visit_type_data = {'I': '住院', 'O': '门诊', 'E': '体检', 'P': '急诊'}
    visit_type_code = random.choice(['O', 'E', 'I', 'P'])
    visit_type = visit_type_data[visit_type_code]

    adjust_sub_class_code = random.choice(['135152', '135148', '135149', '135169', '135147', '135168'])

    sur_name = random.choice(getattr(GetData, 'sur_name'))
    s_name = random.choice(getattr(GetData, 'name'))
    patient_name = sur_name + s_name

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    oper_num = random.randint(1, 20)

    diag_code_group = random.choice(
        ['O70.1', 'O70.2', 'O73.1', 'O86.0', 'I26.9', 'I82.8', 'A40.0', 'T81.0', 'T81.3', 'R96.0', 'J96.0','E89.0','T81.4','T81.5','T88.2','J95.0','T81.2','N17.0','T87.0','T81.1','O70.9','O73.1','O73.1','O95.9'])

    oper_code_group = random.choice(
        ['O70.1', 'O70.2', 'O73.1', 'O86.0', 'I26.9', 'I82.8', 'A40.0', 'T81.0', 'T81.3', 'R96.0', 'J96.0','E89.0','T81.4','T81.5','T88.2','J95.0','T81.2','N17.0','T87.0','T81.1','O70.9','O73.1','O73.1','O95.9','O72.2','A34.1'])

    n = random.randint(20, 25)
    out_main_diag_code = drgs_data[n][1]
    out_main_diag_name = drgs_data[n][0]

    out_way_name = random.choice(['死亡', '危重', '正常'])

    again_in_days = round(random.uniform(1, 20), 2)
    day31_again_in_hospital = random.randint(1, 20)
    baby_flag = random.choice([1,0])


    # 指定日期 转换
    data = random.randint(1, 12)
    get_time = '2020-{0}-05 08:00:00.000000'.format(data)
    now_time = datetime.strptime(get_time, '%Y-%m-%d %H:%M:%S.%f')

    # # 时间统一用
    # now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-10, 14), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset

    update_time = real_time

    sql_3 = '''
    INSERT INTO source.new_case_base (case_id, org_code, source_app, source_case_id, source_visit_id, visit_type_id,
                                   visit_type, visit_type_code, source_patient_id, patient_name, medical_payment_id,
                                   medical_payment_name, in_num, sex_id, sex_code, sex_name, birth_date, age, age_year,
                                   age_month, age_day, age_group_id, age_group_code, age_group_name, marriage_id,
                                   marriage_code, marriage_name, profession_id, profession, birth_address_province,
                                   birth_address_city, nation_name, country_name, idno, work_address, work_phone,
                                   work_zip, account_address, account_address_district, contact_name,
                                   contact_relation_name, contact_address, contact_phone, in_time, out_time, in_dept_id,
                                   in_dept_name, shift_dept_id, shift_dept_name, out_dept_id, out_dept_name, in_ward_id,
                                   in_ward_name, out_ward_id, out_ward_name, bed_doc_id, bed_doc_name, in_days,
                                   in_state, in_diag_date, write_date, clinic_diag_name, in_diag_name, in_diag_code,
                                   infection_diag_code, infection_diag_name, infection_outcome, pathology_dig_code,
                                   pathology_diag_name, injury_poisoning_code, injury_poisoning_name, allergy_flag,
                                   allergy_name, op_dis_conform, in_dis_conform, pre_post_conform,
                                   clinic_pathology_conform, radiation_pathology_conform, frozen_paraffin_confrom,
                                   kideny_therioma_confrom, liver_therioma_confrom, lung_therioma_confrom,
                                   stomach_therioma_confrom, rectum_therioma_confrom, colon_therioma_confrom, hbsag,
                                   hcvab, hivab, salvage_num, succ_num, body_check, first_demo_flag, follow_flag,
                                   follow_week, follow_month, follow_year, demo_flag, bedsore_flag, accident_flag,
                                   mistake_flag, abo_id, abo_name, rh_id, rh_name, reaction_blood, rbc_blood_num,
                                   plasma_blood_num, whole_blood_num, other_blood_num, platelet_blood_num,
                                   dept_chief_doc_name, director_doc_name, attending_doc_id, attending_doc_name,
                                   resident_name, refresher_doc_name, graduate_doc_name, practice_doc_name,
                                   coding_oper_name, case_quality, qc_nurse_name, qc_doc_name, in_source_name,
                                   special_care_days, first_care_days, second_care_days, third_care_days, icu_days,
                                   ccu_days, health_card_no, baby_flag, birth_weight, transfusion_times, infusion_num,
                                   infusion_reaction_flag, again_in_days, peri_oper_dead_flag, pat_giveup_flag,
                                   out_way_id, out_way_code, out_way_name, fall_flag, fall_level,
                                   iatrogenic_pneumothorax_flag, iatrogenic_punctures_flag, hemodialysis_flag,
                                   hemodialysis_infec_flag, pci_and_cabg_flag, same_dis_return_flag,
                                   day31_again_in_hospital, serious_flag, critical_flag, intractable_flag, is_infection,
                                   oper_flag, main_oper_dept_id, main_oper_dept_name, site_infec_flag, forward_flag,
                                   oper_2day_return_flag, oper_31day_return_flag, oper_complication_flag,
                                   plan_return_flag, lung_infec_flag, foreign_bodies_left_flag, in_total_cost, bed_cost,
                                   service_care_cost, west_medicine_cost, cnmedicine_cost, cnmedicine_herbs_cost,
                                   diagnose_pacs_cost, diagnose_lab_cost, oxygen_cost, blood_cost, service_cost,
                                   treat_operate_cost, deliver_cost, check_cost, treat_anesthesia_cost, infant_cost,
                                   extrabed_cost, heat_cost, air_cost, clean_cost, other_cost, service_other_cost,
                                   other_cost2, service_operation_cost, in_selffinance_cost, diagnose_pathology_cost,
                                   diagnose_clinical_cost, treat_non_operate_cost, treat_physical_cost,
                                   treat_operate_all_cost, rehabilitation_cost, cntreat_all_cost,
                                   west_medicine_anti_cost, blood_albumin_cost, blood_globulin_cost,
                                   blood_clotting_cost, blood_cell_cost, material_check_cost, material_treat_cost,
                                   out_main_diag_code, out_main_diag_name, out_main_in_condition, out_main_outcome_name,
                                   out_main_outcome_code, main_operation_time, main_operation_code, main_operation_name,
                                   main_operation_doc_name, main_helper1_name, main_helper2_name, main_anes_type_name,
                                   main_incision_heal_name, main_anes_doc_name, main_incision_type_name,
                                   main_pre2h_durg_flag, main_operation_class_code, main_operation_class_name,
                                   main_peri_flag, main_anes_level, main_duration, main_table_num, main_nnis_level,
                                   main_level_name, main_return_flag, main_site_infec_flag, main_oper_flag,
                                   medical_group_code, medical_group_name, day_surgery_flag, icdlowrisk_flag,
                                   diag_code_group, diag_name_group, oper_code_group, oper_name_group, oper_num, str1,
                                   str2, str3, str4, str5, str6, str7, str8, str9, str10)
VALUES ({0}, '46919132', 'tj_his3', '2', '3722|20210902', 3, '住院', 'I', '380', '徐舚', null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, '{2}', null, null, null, null, null,
        null, null, null, null, '死亡', null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, {9}, null, null, null, null, {7}, null, null, null, null, '{6}',
        null, null, null, null, null, null, null, null, {8}, null, null, null, null, 1, null, null, null, null, 1, 1,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, '{4}', '{5}', null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 1,
        '{3}', null, '{10}', null, {1}, null, null, null, null, null, null, null, null, null, null);
        '''.format(max_case_id, oper_num, update_time, diag_code_group, out_main_diag_code, out_main_diag_name,
                   out_way_name, again_in_days, day31_again_in_hospital,baby_flag,oper_code_group)

    mysql_bi.insert(sql_3)
    print(i)
