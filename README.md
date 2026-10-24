# Hệ thống Liên kết & Gợi ý Đa đối tượng (Courses Recommendation System)

> **Đề tài:** Hệ thống Liên kết & Gợi ý Đa đối tượng JD (Việc làm) – CV (Ứng viên) – Course (Khóa học).  
> **Kiến trúc:** MLOps / Data Science chuẩn hóa quy trình từ thu thập, tiền xử lý, trích xuất thực thể (NER), học biểu diễn (Bi-Encoder Triplet) đến tìm kiếm lai (Hybrid Search: Dense + BM25).

---

## 📌 Cấu trúc dự án

```text
TLCN-KLTN/
│
├── .gitignore                      # Cấu hình loại trừ file rác, dữ liệu nặng và mô hình
├── .env.example                    # File mẫu biến môi trường (API keys)
├── README.md                       # Tài liệu hướng dẫn dự án
├── requirements.txt                # Danh sách thư viện phụ thuộc
│
├── configs/                        # File cấu hình tham số huấn luyện và hệ thống
│
├── data/                           # Dữ liệu dự án (quản lý qua Kaggle/Drive, chỉ giữ khung thư mục)
│   ├── raw/                        # Dữ liệu thô thu thập từ crawlers
│   │   ├── courses/                # Khóa học (Coursera, Udemy, edX, DataCamp, FutureLearn)
│   │   ├── jobs/                   # Tin tuyển dụng (TopCV, ITviec, VietnamWorks, CareerViet,...)
│   │   └── cv/                     # Hồ sơ ứng viên mẫu
│   │
│   ├── processed/                  # Dữ liệu đã làm sạch và chuẩn hóa schema
│   │   ├── courses/
│   │   ├── jobs/
│   │   └── cv/
│   │
│   ├── ner_datasets/               # Dữ liệu gán nhãn thực thể (Entity Recognition)
│   └── embedding_datasets/         # Dữ liệu Triplet huấn luyện Bi-Encoder
│
├── notebooks/                      # Jupyter Notebooks nghiên cứu, thử nghiệm & EDA
│
├── src/                            # Mã nguồn chính của hệ thống
│   ├── __init__.py
│   ├── crawlers/                   # Module cào dữ liệu
│   │   ├── __init__.py
│   │   ├── courses/                # Crawlers khóa học
│   │   └── jobs/                   # Crawlers tin tuyển dụng
│   │
│   ├── preprocessing/              # Module tiền xử lý và chuẩn hóa dữ liệu
│   │   ├── __init__.py
│   │   ├── courses/                # Làm sạch, lọc kỹ năng & level khóa học
│   │   ├── jobs/                   # Hợp nhất schema & ID tin tuyển dụng
│   │   └── cv/                     # Trích xuất và chuẩn hóa CV
│   │
│   ├── ner/                        # Module nhận dạng thực thể (Skills, Degrees, Experience)
│   └── embeddings/                 # Module tạo cặp Triplet, huấn luyện Bi-Encoder & Hybrid Search
│
├── models/                         # Trọng số mô hình sau huấn luyện (weights / checkpoints)
│   ├── ner_model/                  # Checkpoint mô hình NER
│   ├── embedding_model/            # Checkpoint mô hình Bi-Encoder Embedding
│   └── hybrid_model/               # Cấu hình chỉ mục lai Dense + BM25
│
└── scripts/                        # Scripts thực thi quy trình đầu cuối (End-to-End)
    ├── run_crawlers.py             # Script chạy cào dữ liệu
    ├── run_etl_pipeline.py         # Script chạy quy trình ETL tiền xử lý
    ├── run_train_ner.py            # Script huấn luyện mô hình NER
    ├── run_train_embedding.py      # Script huấn luyện mô hình Embedding Triplet
    └── run_demo.py                 # Script chạy thử nghiệm / Demo gợi ý
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
