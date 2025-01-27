
dentweb_mapping = {
    "진료일": "treatment_date",
    "차트번호": "chart_number",
    "이름": "name",
    "보험구분": "insurance_type",
    "수입집계": "income_summary",
    "진료의사": "doctor_in_charge",
    "어시스트": "assistant",
    "당일접수": "same_day_registration",
    "수납자": "payment_collector",
    "총진료비": "total_treatment_cost",
    "청구액": "claim_amount",
    "본인부담금": "personal_expense",
    "비급여": "non_covered_expense",
    "부가가치세": "vat",
    "할인액": "discount_amount",
    "총수납액": "total_payment_received",
    "카드수납": "card_payment",
    "현금수납": "cash_payment",
    "기타_온라인": "other_online_payment",
    "현영발행액": "cash_receipt_issued_amount",
    "건강생활유지비승인": "health_living_expense_approval",
    "미수_선수": "receivable_prepaid",
    "총미수_선수": "total_receivable_prepaid",
    "진료비구분": "treatment_cost_category",
    "진료내역": "treatment_details",
    "메모": "memo",
    "최초내원": "first_visit_date",
    "내원경로": "visit_path",
    "고객성향": "customer_preference",
    "고객구분": "customer_category",
    "고객구분2": "customer_category_2",
    "리콜구분": "recall_category",
}


# 한글 -> 영어 변환 함수
def convert_to_english(korean_columns):
    return [dentweb_mapping.get(col, col) for col in korean_columns]

# 영어 -> 한글 변환 함수
def convert_to_korean(english_columns):
    reverse_mapping = {v: k for k, v in dentweb_mapping.items()}
    return [dentweb_mapping.get(col, col) for col in english_columns]