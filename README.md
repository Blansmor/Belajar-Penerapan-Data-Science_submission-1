# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding
Perusahaan Jaya Jaya Maju menghadapi masalah tingginya tingkat keluarnya karyawan (attrition). Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Oleh karena itu, perlu dianalisis faktor-faktor yang mempengaruhi tingkat keluarnya karyawan untuk membantu departemen HR dalam mengurangi tingkat attrition.

### Permasalahan Bisnis
Tingkat keluarnya karyawan yang tinggi di perusahaan Jaya Jaya Maju menyebabkan berbagai masalah bisnis yang signifikan. Berikut adalah beberapa permasalahan bisnis utama yang dihadapi oleh perusahaan:

1. Produktivitas Menurun
    Kehilangan karyawan dapat mengakibatkan penurunan produktivitas tim dan keseluruhan perusahaan. Pengalaman dan pengetahuan yang dimiliki karyawan lama sulit untuk digantikan dalam waktu singkat.
2. Gangguan dalam Operasional
    Kehilangan karyawan secara tiba-tiba dapat mengganggu alur kerja dan menyebabkan proyek atau tugas tertunda. Ini dapat berdampak negatif pada kualitas layanan yang diberikan kepada klien.
3. Kepuasan Karyawan Menurun
    Tingginya tingkat keluarnya karyawan dapat mempengaruhi moral dan kepuasan karyawan yang masih bertahan.
4. Reputasi Perusahaan Terancam
    Jika tingkat keluarnya karyawan terus tinggi, reputasi perusahaan sebagai tempat kerja yang stabil dan mendukung bisa terancam. Ini dapat mempengaruhi perusahaan untuk mencari pekerja dimasa depan

### Cakupan Proyek
1. Mengumpulkan dan memproses data karyawan.
2. Menganalisis data untuk menemukan pola dan faktor-faktor yang mempengaruhi keluarnya karyawan.
3. Membangun model prediktif menggunakan algoritma Logistic Regression.
4. Membuat dashboard bisnis untuk memvisualisasikan temuan dan prediksi.
5. Memberikan rekomendasi tindakan berdasarkan hasil analisis.

### Persiapan
Berikut adalah tahapan untuk menyiapkannya:

sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Setup environment:
Apabila menginstal Python melalui Anaconda ataupun miniconda, Anda dapat menggunakan conda sebagai package manager dan environment management system. Berikut merupakan tahapan dalam membuat virtual environment menggunakan conda untuk melakukan prediksi.

1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.
    ```
     conda create --name prediksi_attrition python=3.9
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate prediksi_attrition
    ```
4. Instal semua library yang dibutuhkan menggunakan perintah berikut.
    ```
    pip install numpy==1.24.4 pandas==2.1.4 matplotlib==3.7.5 seaborn==0.13.2 scikit-learn==1.4.0 SQLAlchemy==2.0.30
    ```
5. Buka jupyter-notebook dengan menjalankan perintah berikut.
    ```
    jupyter-notebook
    ```
6. Buka file python prediction.py
7. Masukkan data yang ingin diprediksi pada variabel X_new
8. Tekan tombol run code
8. Hasil prediksi akan keluar

## Business Dashboard
Dashboard bisnis dibuat untuk memvisualisasikan data karyawan, tingkat keluarnya karyawan, dan faktor-faktor yang mempengaruhi tingginya attrition rate. Dashboard ini akan menampilkan faktor demografis dan penghasilan, faktor pekerjaan dan kepuasan, faktor
keseimbangan kerja dan kehidupan, dan faktor lainnya yang mempengaruhi tingginya attrition rate.

## Conclusion
Karyawan yang keluar cenderung memiliki umur yang muda dan belum menikah, memiliki gaji yang lebih sedikit tetapi mempunyai penghasilan lain yang lebih besar, tidak dapat menyeimbangkan antara pekerjaan dan kehidupannya, karyawan yang tidak nyaman dengan lingkungan kerjanya terutama tidak nyaman dengan atasannya, karyawan yang jarang promosi, dan banyak karyawan yang keluar dari bidang pekerjaan teknisi laboratorium, human resources, dan research scientist. Banyak juga karyawan yang keluar dari latar belakang pendidikan teknik dan marketing.

### Rekomendasi Action Items
Berikut adalah rekomendasi yang dapat dilakukan perusahaan Jaya Jaya Maju untuk mengurangi tingkat attrition:

1. BusinessTravel:

    Evaluasi kebutuhan BusinessTravel secara rutin dan pertimbangkan alternatif seperti remote work untuk mengurangi beban perjalanan yang dapat mempengaruhi kepuasan karyawan.
2. Department:

    Lakukan analisis lebih lanjut mengenai faktor-faktor yang mempengaruhi attrition di R&D dan Sales. Mungkin perlu meninjau ulang budaya kerja atau program pengembangan karir di departemen ini.
3. Education Level dan Field:

    Tinjau kembali program pelatihan atau kesempatan pengembangan karir untuk karyawan. Fokus pada kategori EducationField seperti Life Sciences dan Medical untuk meningkatkan retensi.
4. Environment Satisfaction:

    Perhatikan karyawan yang mengalami tingkat kepuasan lingkungan rendah. Tinjau faktor-faktor penyebab dan tawarkan solusi yang dapat meningkatkan kepuasan kerja, seperti program kesejahteraan atau peningkatan komunikasi internal.
5. Gender:

    Tinjau ulang tantangan atau masalah spesifik yang dihadapi oleh karyawan laki-laki. Pastikan kebijakan dan program di perusahaan mendukung kebutuhan dan harapan dari semua karyawan.
6. Job Role dan Level:

    Analisis lebih lanjut pada karyawan dengan peran seperti Laboratory Technician, Sales Executive, dan Research Scientist. Mungkin diperlukan peninjauan ulang terhadap beban kerja, kesempatan pengembangan, atau kebutuhan kompensasi.
7. Work-Life Balance dan Overtime:

    Evaluasi dampak jam kerja tambahan (overtime) terhadap tingkat attrition. Pertimbangkan kebijakan yang lebih baik untuk mengelola beban kerja dan mendorong keseimbangan kehidupan kerja yang lebih baik.
8. Performance Rating dan Job Satisfaction:

    Tawarkan feedback yang jelas dan dukungan pengembangan untuk karyawan yang mungkin merasa kurang puas atau merasa kurang dihargai.
9. Marital Status:

    Perhatikan tingkat attrition yang tinggi pada karyawan status single. Mungkin perlu meninjau ulang program-program dukungan sosial atau kesejahteraan untuk memenuhi kebutuhan mereka.
10. Stability in Role dan Loyalty to Manager:

    Tinjau pengalaman karyawan dalam peran dan hubungan dengan manajer mereka. Berikan pelatihan kepemimpinan yang mungkin diperlukan untuk memperbaiki hubungan dan stabilitas di tempat kerja.
11. Compensation and Benefits:

    Pastikan bahwa kompensasi dan manfaat perusahaan memadai untuk mempertahankan karyawan. Tinjau kembali struktur kompensasi untuk memastikan adil dan sesuai dengan industri.
12. Training and Career Development:

    Tingkatkan investasi dalam pelatihan dan pengembangan karir. Pastikan setiap karyawan memiliki akses yang setara terhadap peluang pengembangan yang dapat meningkatkan keterlibatan dan retensi.

## Email dan password Metabase
Email: root@mail.com
Password: root123
