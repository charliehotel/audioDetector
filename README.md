WebRTC VAD Audio Detector

⸻

📌 Overview (개요)

This project provides a simple Python script that detects speech and silence durations from a WAV audio file using the Google WebRTC Voice Activity Detector (VAD).
It is lightweight, fast, and suitable for both offline analysis and real-time speech detection.

이 프로젝트는 **Google WebRTC 음성 활동 감지기(VAD)**를 사용하여 WAV 오디오 파일에서 사람의 음성 구간과 침묵 구간을 감지하는 간단한 Python 스크립트입니다.
가볍고 빠르며, 오프라인 분석 및 실시간 음성 감지에도 활용할 수 있습니다.

⸻

✨ Features (주요 기능)  
	•	✅ Detects speech segments and silence durations (음성 구간 및 침묵 구간 감지)  
	•	✅ Adjustable sensitivity levels (0–3) (민감도 조절 가능)  
	•	✅ Lightweight and fast (가볍고 빠른 성능)  
	•	✅ MIT License (오픈소스 MIT 라이선스)

⸻

🛠 Installation (설치 방법)

	pip install webrtcvad

⸻

🚀 Usage (사용 방법)

1.	Place your WAV file in the audioDetector folder.
2.	Run the script:

	python detector.py

3.	Example output:

	Total duration: 120.50 seconds  
	Speech duration: 45.30 seconds  
	Silence duration: 75.20 seconds

⸻

📄 License (라이선스 안내)

This project is licensed under the MIT License.
You are free to use, copy, modify, and distribute this software, provided that you include the copyright notice and license text in all copies or substantial portions of the Software.
See the LICENSE file for details.

이 프로젝트는 MIT 라이선스로 배포됩니다.
저작권 고지와 라이선스 사본을 포함하는 조건으로, 자유롭게 사용, 복사, 수정, 배포할 수 있습니다.
자세한 내용은 LICENSE 파일을 참고하세요.

⸻

🙌 Acknowledgements (감사의 말)  
	•	Google WebRTC Project for providing the VAD algorithm  
	•	Python webrtcvad library maintainers  
	•	오픈소스 커뮤니티의 기여에 감사드립니다.
