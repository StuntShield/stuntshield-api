main_config = {
    'BASE_URL': 'http://localhost',
    'PORT': '5000',
    'UPLOAD_FOLDER_STUNTING': './assets/users_uploads/data_stunting',
    'UPLOAD_FOLDER_WEIGHT': './assets/users_uploads/data_weight',
    'UPLOAD_FOLDER_IDEAL_024': './assets/users_uploads/data_ideal/umur_0_24_bulan',
    'UPLOAD_FOLDER_IDEAL_2460': './assets/users_uploads/data_ideal/umur_24_60_bulan',
    'OPENAI_API_KEY': '',
    # 'GCS_CREDENTIALS': '',
    # 'GCP_CREDIT': ''
}

model_config = {
    'MODEL_CLASSIFICATION_STUNTING': './assets/ml_models/stunting_prediction.h5',
    'MODEL_CLASSIFICATION_WEIGHT': './assets/ml_models/weight_prediction.h5',
    'MODEL_CLASSIFICATION_IDEAL_024': './assets/ml_models/ideal_prediction_024.h5',
    'MODEL_CLASSIFICATION_IDEAL_2460': './assets/ml_models/ideal_prediction_2460.h5',
    # 'OPENAI_API_KEY': ''
}
