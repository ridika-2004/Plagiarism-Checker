<a name="top"></a>

<h1 align="center">
  $\Huge\textbf{\color{#5E81AC}{Plagiarism Checker}}$
</h1>

$${\color{#88C0D0}A \space simple \space Django-based \space web \space app \space to \space detect \space plagiarism \space in \space user-submitted \space text.}$$

> <img src="https://github.com/user-attachments/assets/99ecbf4a-4e0b-451e-a2c0-2f65e2938a34" align="right" width="280px">

A clean, minimal plagiarism checker that uses the [GoWinston.ai](https://dev.gowinston.ai) API to fetch real-time plagiarism scores and highlight matching sources.  
Perfect for educational projects or demos using Django and REST API integration.

<br>

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Winston.ai](https://img.shields.io/badge/API-GoWinston.ai-6A1B9A?style=for-the-badge&logo=swagger)


## File Structure

<details>
  <summary>Click to view</summary>
  
  ```console
  plagiarism-checker/
├── checker/
│ ├── templates/
│ │ └── index.html
│ ├── views.py
│ └── ...
├── plagiarism_checker/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── static/ (optional)
├── manage.py
├── requirements.txt
├── Procfile (for deployment)
├── render.yaml (for deployment)
└── README.md
```

</details>

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/your-username/plagiarism-checker.git
cd plagiarism-checker
```

Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate    # On Windows: .\env\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Create `.env` file:
```bash
DJANGO_SECRET_KEY=your-secret-key
WINSTON_API_TOKEN=your-winston-token
```

Run the development server:
```bash
python manage.py runserver
```
Open your browser at `http://127.0.0.1:8000/`

## Author
| Name          | GitHub                                         | Role      |
| ------------- | ---------------------------------------------- | --------- |
| Ridika Naznin | [@ridika-2004](https://github.com/ridika-2004) | Developer |
