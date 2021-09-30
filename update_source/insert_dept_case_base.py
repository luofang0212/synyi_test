#!/usr/bin/env python
# -*- coding:utf-8 -*-

from util.dbClickhouse_util import ClickHouseDb
from util.dbPlsql_util_system import PlSqlDb as PlSqlDb2
from util.dbPlsql_util_bi import PlSqlDbBI
import random
from datetime import datetime,timedelta
from update_source.get_data import GetData

mysql1 = PlSqlDbBI()
sql_1 = '''select max(case_id) from source.case_base;'''
res_1 = mysql1.query(sql_1)

max_case_id = res_1[0][0] + 1

mysql = PlSqlDb2()

sql_2 = '''select dept_id,dept_name,normalized_dept_name,normalized_dept_id,source_app
from system.normalized_department;
'''

res_2 = mysql.query(sql_2)

# dept_id = res_2[3][0]
# dept_name = res_2[3][1]
# normalized_dept_name = res_2[3][2]
# normalized_dept_id  = res_2[3][3]
# source_app = res_2[3][4]
print(len(res_2))
print(res_2)

for i in range(1,1209):
    max_case_id = max_case_id + 1

    res_2 = mysql.query(sql_2)
    dept_id = res_2[i][0]
    dept_name = res_2[i][1]
    normalized_dept_name = res_2[i][2]
    normalized_dept_id = res_2[i][3]
    source_app = res_2[i][4]

    doc_id = random.choice(GetData.doc_id)
    doc_data = GetData.doc_data
    doc_name = doc_data[doc_id]

    # 指定日期 转换
    # get_time = '2021-08-10 00:00:00.000000'
    # now_time = datetime.strptime(get_time,'%Y-%m-%d %H:%M:%S.%f')
    now_time = datetime.now()
    # 根据当前时间 去计算便宜时间，随机生成时间
    # hours_data = random.randint(-10,14)
    hours_data = round(random.uniform(-15, 9), 2)
    offset = timedelta(hours=hours_data)
    real_time = now_time + offset
    update_time = real_time

    sql_3 = '''insert into source.case_base (case_id, org_code, source_app, source_case_id, source_visit_id, source_patient_id,
                              patient_name, medical_payment_id, medical_payment_name, in_num, sex_id, sex_name,
                              birth_date, age, age_year, age_month, age_day, marriage_id, marriage_name, profession_id,
                              profession, birth_address_province, birth_address_city, nation_name, country_name, idno,
                              work_address, work_phone, work_zip, account_address, account_address_district,
                              contact_name, contact_relation_name, contact_address, contact_phone, in_time, out_time,
                              in_dept_id, in_dept_name, shift_dept_id, shift_dept_name, out_dept_id, out_dept_name,
                              in_ward_id, in_ward_name, out_ward_id, out_ward_name, in_days, in_state, write_date,
                              clinic_diag_name, in_diag_name, in_diag_code, infection_diag_code, infection_diag_name,
                              infection_outcome, pathology_dig_code, pathology_diag_name, injury_poisoning_code,
                              injury_poisoning_name, allergy_name, op_dis_conform, in_dis_conform, pre_post_conform,
                              clinic_pathology_conform, radiation_pathology_conform, frozen_paraffin_confrom,
                              kideny_therioma_confrom, liver_therioma_confrom, lung_therioma_confrom,
                              stomach_therioma_confrom, rectum_therioma_confrom, colon_therioma_confrom, hbsag, hcvab,
                              hivab, salvage_num, succ_num, body_check, first_demo_flag, follow_flag, follow_week,
                              follow_month, follow_year, demo_flag, bedsore_flag, accident_flag, mistake_flag, abo_id,
                              abo_name, rh_id, rh_name, reaction_blood, rbc_blood_num, plasma_blood_num,
                              whole_blood_num, other_blood_num, platelet_blood_num, dept_chief_doc_name,
                              director_doc_name, attending_doc_name, resident_name, refresher_doc_name,
                              graduate_doc_name, practice_doc_name, coding_oper_name, case_quality, qc_nurse_name,
                              qc_doc_name, in_source_name, special_care_days, first_care_days, second_care_days,
                              third_care_days, icu_days, ccu_days, health_card_no, birth_weight, transfusion_times,
                              infusion_num, infusion_reaction_flag, again_in_days, peri_oper_dead_flag, pat_giveup_flag,
                              out_way_name, fall_flag, fall_level, iatrogenic_pneumothorax_flag,
                              iatrogenic_punctures_flag, hemodialysis_flag, hemodialysis_infec_flag, pci_and_cabg_flag,
                              same_dis_return_flag, again_in_hospital, serious_flag, critical_flag, intractable_flag,
                              is_infection, oper_flag, main_oper_dept_name, site_infec_flag, forward_flag,
                              oper_return_flag, oper_complication_flag, foreign_bodies_left_flag, in_total_cost,
                              bed_cost, service_care_cost, west_medicine_cost, cnmedicine_cost, cnmedicine_herbs_cost,
                              diagnose_pacs_cost, diagnose_lab_cost, oxygen_cost, blood_cost, service_cost,
                              treat_operate_cost, deliver_cost, check_cost, treat_anesthesia_cost, infant_cost,
                              extrabed_cost, heat_cost, air_cost, clean_cost, other_cost, service_other_cost,
                              other_cost2, service_operation_cost, in_selffinance_cost, diagnose_pathology_cost,
                              diagnose_clinical_cost, treat_non_operate_cost, treat_physical_cost,
                              treat_operate_all_cost, rehabilitation_cost, cntreat_all_cost, west_medicine_anti_cost,
                              blood_albumin_cost, blood_globulin_cost, blood_clotting_cost, blood_cell_cost,
                              material_check_cost, material_treat_cost, out_main_diag_code, out_main_diag_name,
                              out_main_in_condition, out_main_outcome_name, other_diag1_code, other_diag1_name,
                              other_diag1_in_condition, other_diag1_outcome, other_diag2_code, other_diag2_name,
                              other_diag2_in_condition, other_diag2_outcome, other_diag3_code, other_diag3_name,
                              other_diag3_in_condition, other_diag3_outcome, other_diag4_code, other_diag4_name,
                              other_diag4_in_condition, other_diag4_outcome, other_diag5_code, other_diag5_name,
                              other_diag5_in_condition, other_diag5_outcome, other_diag6_code, other_diag6_name,
                              other_diag6_in_condition, other_diag6_outcome, other_diag7_code, other_diag7_name,
                              other_diag7_in_condition, other_diag7_outcome, other_diag8_code, other_diag8_name,
                              other_diag8_in_condition, other_diag8_outcome, other_diag9_code, other_diag9_name,
                              other_diag9_in_condition, other_diag9_outcome, other_diag10_code, other_diag10_name,
                              other_diag10_in_condition, other_diag10_outcome, other_diag11_code, other_diag11_name,
                              other_diag11_in_condition, other_diag11_outcome, other_diag12_code, other_diag12_name,
                              other_diag12_in_condition, other_diag12_outcome, other_diag13_code, other_diag13_name,
                              other_diag13_in_condition, other_diag13_outcome, other_diag14_code, other_diag14_name,
                              other_diag14_in_condition, other_diag14_outcome, other_diag15_code, other_diag15_name,
                              other_diag15_in_condition, other_diag15_outcome, other_diag16_code, other_diag16_name,
                              other_diag16_in_condition, other_diag16_outcome, other_diag17_code, other_diag17_name,
                              other_diag17_in_condition, other_diag17_outcome, other_diag18_code, other_diag18_name,
                              other_diag18_in_condition, other_diag18_outcome, other_diag19_code, other_diag19_name,
                              other_diag19_in_condition, other_diag19_outcome, other_diag20_code, other_diag20_name,
                              other_diag20_in_condition, other_diag20_outcome, main_operation_time, main_operation_code,
                              main_operation_name, main_operation_doc_name, main_helper1_name, main_helper2_name,
                              main_anes_type_name, main_incision_heal_name, main_anes_doc_name, main_incision_type_name,
                              main_pre2h_durg_flag, main_peri_flag, main_anes_level, main_duration, main_table_num,
                              main_nnis_level, main_return_flag, main_site_infec_flag, main_oper_flag,
                              oper2_operation_time, oper2_operation_code, oper2_operation_name,
                              oper2_operation_doc_name, oper2_helper1_name, oper2_helper2_name, oper2_anes_type_name,
                              oper2_incision_heal_name, oper2_anes_doc_name, oper2_incision_type_name,
                              oper2_pre2h_durg_flag, oper2_peri_flag, oper2_anes_level, oper2_duration, oper2_table_num,
                              oper2_nnis_level, oper2_return_flag, oper2_site_infec_flag, oper2_oper_flag,
                              oper3_operation_time, oper3_operation_code, oper3_operation_name,
                              oper3_operation_doc_name, oper3_helper1_name, oper3_helper2_name, oper3_anes_type_name,
                              oper3_incision_heal_name, oper3_anes_doc_name, oper3_incision_type_name,
                              oper3_pre2h_durg_flag, oper3_peri_flag, oper3_anes_level, oper3_duration, oper3_table_num,
                              oper3_nnis_level, oper3_return_flag, oper3_site_infec_flag, oper3_oper_flag,
                              oper4_operation_time, oper4_operation_code, oper4_operation_name,
                              oper4_operation_doc_name, oper4_helper1_name, oper4_helper2_name, oper4_anes_type_name,
                              oper4_incision_heal_name, oper4_anes_doc_name, oper4_incision_type_name,
                              oper4_pre2h_durg_flag, oper4_peri_flag, oper4_anes_level, oper4_duration, oper4_table_num,
                              oper4_nnis_level, oper4_return_flag, oper4_site_infec_flag, oper4_oper_flag,
                              oper5_operation_time, oper5_operation_code, oper5_operation_name,
                              oper5_operation_doc_name, oper5_helper1_name, oper5_helper2_name, oper5_anes_type_name,
                              oper5_incision_heal_name, oper5_anes_doc_name, oper5_incision_type_name,
                              oper5_pre2h_durg_flag, oper5_peri_flag, oper5_anes_level, oper5_duration, oper5_table_num,
                              oper5_nnis_level, oper5_return_flag, oper5_site_infec_flag, oper5_oper_flag,
                              oper6_operation_time, oper6_operation_code, oper6_operation_name,
                              oper6_operation_doc_name, oper6_helper1_name, oper6_helper2_name, oper6_anes_type_name,
                              oper6_incision_heal_name, oper6_anes_doc_name, oper6_incision_type_name, oper6_anes_level,
                              oper6_nnis_level, oper6_oper_flag, oper7_operation_time, oper7_operation_code,
                              oper7_operation_name, oper7_operation_doc_name, oper7_helper1_name, oper7_helper2_name,
                              oper7_anes_type_name, oper7_incision_heal_name, oper7_anes_doc_name,
                              oper7_incision_type_name, oper7_anes_level, oper7_nnis_level, oper7_oper_flag,
                              oper8_operation_time, oper8_operation_code, oper8_operation_name,
                              oper8_operation_doc_name, oper8_helper1_name, oper8_helper2_name, oper8_anes_type_name,
                              oper8_incision_heal_name, oper8_anes_doc_name, oper8_incision_type_name, oper8_anes_level,
                              oper8_nnis_level, oper8_oper_flag, oper9_operation_time, oper9_operation_code,
                              oper9_operation_name, oper9_operation_doc_name, oper9_helper1_name, oper9_helper2_name,
                              oper9_anes_type_name, oper9_incision_heal_name, oper9_anes_doc_name,
                              oper9_incision_type_name, oper9_anes_level, oper9_nnis_level, oper9_oper_flag,
                              oper10_operation_time, oper10_operation_code, oper10_operation_name,
                              oper10_operation_doc_name, oper10_helper1_name, oper10_helper2_name,
                              oper10_anes_type_name, oper10_incision_heal_name, oper10_anes_doc_name,
                              oper10_incision_type_name, oper10_anes_level, oper10_nnis_level, oper10_oper_flag,
                              main_operation_class_code, main_level_name, oper2_operation_class, oper2_level_name,
                              oper3_operation_class, oper3_level_name, oper4_operation_class, oper4_level_name,
                              oper5_operation_class, oper5_level_name, oper6_operation_class, oper6_level_name,
                              oper7_operation_class, oper7_level_name, oper8_operation_class, oper8_level_name,
                              oper9_operation_class, oper9_level_name, oper10_operation_class, oper10_level_name,
                              attending_doc_id, bed_doc_id, bed_doc_name, in_diag_date, visit_type_id, visit_type,
                              visit_type_code, sex_code, marriage_code, out_way_id, out_way_code, plan_return_flag,
                              lung_infec_flag, age_group_id, age_group_code, age_group_name, allergy_flag,
                              main_operation_class_name, out_main_outcome_code, medical_group_code, medical_group_name,
                              patient_id, normalized_in_dept_id, normalized_in_dept_name, normalized_out_dept_id,
                              normalized_out_dept_name, str1, str2, str3, str4, str5, str6, str7, str8, str9, str10,
                              main_oper_dept_id, drg_code, drg_name, rw, mdc_code, mdc_name, adrg_code, adrg_name,
                              low_risk_group_flag, charge_consumption_standard, time_consumption_standard)
values ({0}, '46919134-2', '{1}', 1935806002, 1935806002, 60296403, '张凤兰', 140598, '全自费', 2, null, '女性',
        '{2}', 65, 65, 800, 24019, 140602, '已婚', 140566, '农民', '江苏省', '泰州市', '汉族', '中国',
        321086195401282626, '-', 13852621654, 214500, '江苏省泰州市靖江市靖江江阴开发区八圩村前义太庄5号', null, '朱红琴', '女',
        '靖江市靖江江阴开发区八圩村前义太庄5号', 13852621654, '{2}', '{2}', 144, '泌尿外科',
        null, null, {3}, '{4}', 283, '泌尿外科护理单元', 283, '泌尿外科护理单元', 9.0, 3.0, null, '肾结石', '肾结石', 'N20.000', null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, 0, 0, 0, null, null, null, null, null, null, null, null, null, 140586, '未查', 140591, '未查', 0,
        null, null, null, null, null, '刘欣', '姚宝庚', '{8}', '陶湘炜', null, null, null, '姚海燕', '甲', '陈晨', '姚宝庚', '门诊', null,
        5.0, 2.0, null, null, null, 60296403, null, null, null, null, 13.0, null, null, '医嘱离院', null, null, null, null,
        0, null, null, null, 0, 0, 0, 0, 0, 1, '{6}', 0, null, null, 0, null, 20200.1800, 660.0000, 221.7000,
        2880.4800, 58.4000, null, 133.0000, 580.0000, null, null, 732.0000, 6486.0000, null, 629.7000, 873.0000, null,
        null, null, null, null, null, null, null, 435.4000, null, null, 616.7000, 300.0000, 300.0000, 7359.0000,
        168.0000, 180.0000, 773.2400, null, null, 63.6000, null, 59.6700, 504.5300, 'N20.000', '肾结石', '情况不明', '好转',
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, '{2}', 56.0004, '输尿管镜下取异物', '曹滨', '陶湘炜',
        '丁勇', '全麻', '其他', '朱焱林', '0类', null, null, 'IV', null, 1, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, 1, '四级手术', null, null, null, null, null, null, null,
        null, null, null, null, null, null, null, null, null, null, null, {7}, 801, '曹滨', '{2}',
        552, '住院', 'I', 2, 2, 140610, 1, null, 0, 96218, '>65', '>65岁', 0, '择期', 2, '病区医生|0210', '泌尿外科', 828581, 18,
        '泌尿外科', 18, '泌尿外科', null, null, null, null, null, null, null, null, null, null, {5}, null, null, null, null,
        null, null, null, null, null, null);
        '''.format(max_case_id,source_app,update_time,dept_id,dept_name,dept_id,dept_name,doc,doc_name)
    mysql1.insert(sql_3)
    print(i)