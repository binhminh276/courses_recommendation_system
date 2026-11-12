# Hệ thống Liên kết & Gợi ý Đa đối tượng (Courses Recommendation System)

> **Đề tài:** Hệ thống Liên kết & Gợi ý Đa đối tượng JD (Việc làm) – CV (Ứng viên) – Course (Khóa học).  
> **Kiến trúc:** MLOps / Data Science chuẩn hóa quy trình từ thu thập, tiền xử lý, trích xuất thực thể (NER), học biểu diễn (Bi-Encoder Triplet) đến tìm kiếm lai (Hybrid Search: Dense + BM25).

---

## 📌 Cấu trúc dự án

```text
courses_recommendation_system/
├── .gitignore
├── README.md
├── assets/
│   └── ablation_study_comparison.png
├── docs/
│   └── Bao_Cao_He_Thong_Goi_Y_Khoa_Hoc.docx
└── notebooks/
    ├── 01_cv_labelling.ipynb
    ├── 02_training_ner_nlp.ipynb
    ├── 03_create_master_skill_registry_graphdb.ipynb
    ├── 04_hybrid_embedding_training.ipynb
    ├── 05_create_benchmark_and_voting.ipynb
    └── preprocessing_scripts/
        ├── AWS_Preprocessing.py
        ├── Coursera_Preprocessing.py
        └── course_labeled.py
```

---

## 🚀 Hướng dẫn cài đặt & Chạy

### 1. Khởi tạo môi trường ảo Python
Khuyến nghị sử dụng Python 3.10+:

```bash
python -m venv venv
# Trên Windows:
.\venv\Scripts\activate
# Trên Linux / macOS:
source venv/bin/activate
```

### 2. Cài đặt các thư viện phụ thuộc
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Cấu hình biến môi trường
Tạo file `.env` từ file mẫu `.env.example` và điền các khóa API cần thiết:
```bash
cp .env.example .env
```

---

## 🛠️ Sử dụng các Script chính

### 1. Cào dữ liệu (Crawlers)
```bash
python scripts/run_crawlers.py --source all
# Hoặc chỉ cào khóa học / việc làm:
python scripts/run_crawlers.py --source courses
python scripts/run_crawlers.py --source jobs
```

### 2. Tiền xử lý & ETL
```bash
python scripts/run_etl_pipeline.py --target all
```

### 3. Huấn luyện NER & Embedding
```bash
# Huấn luyện mô hình NER
python scripts/run_train_ner.py

# Huấn luyện mô hình Embedding (Triplet Loss)
python scripts/run_train_embedding.py --epochs 3 --batch-size 32
```

### 4. Chạy Demo
```bash
python scripts/run_demo.py --mode cli
```

---

## 📄 License
Dự án được phát triển phục vụ mục đích nghiên cứu học thuật và khóa luận tốt nghiệp.
