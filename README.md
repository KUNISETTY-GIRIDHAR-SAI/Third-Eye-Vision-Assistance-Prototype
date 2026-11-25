# Third Eye — Vision Assistance Prototype

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-Edge%20AI-red)
![Hackathon](https://img.shields.io/badge/SRM%20University%20Hackathon-24hr%20Sprint-purple)
![Status](https://img.shields.io/badge/Status-Prototype%20Completed-success)

## 📌 Project Overview
Built during the **SRM University Hackathon** under **24-hour constraints**, **Third Eye** is an assistive vision prototype designed to empower visually impaired individuals with real-time spatial obstacle detection and natural audio navigation cues.

As the **Data Preparation and Analytical Workflows Lead**, spearheaded the image preprocessing pipeline, contrast enhancement routines, bounding box zone mapping, and spatial proximity algorithms that convert raw video frames into low-latency spoken navigation warnings.

---

## 🚀 Key Features & Hackathon Highlights
- **Real-Time Edge Detection**: Detects common urban obstacles including pedestrians, stairs, pylons, vehicles, and doorways.
- **Tri-Zone Spatial Localization**: Classifies detected obstacles into `Left`, `Center`, or `Right` corridors, with immediate hazard prioritization for objects in the direct walking path.
- **Proximity Estimation**: Heuristic depth estimation based on bounding box scales, providing distance cues in meters without needing expensive LiDAR sensors.
- **Auditory Guidance Synthesis**: Translates spatial coordinates into concise, natural voice prompts (e.g. *"Caution: Pylon directly Center at 1.8 meters. Step slightly Right."*).

---

## 📂 Repository Structure
```
Third-Eye-Vision-Assistance-Prototype/
├── src/
│   ├── data_preparation_workflow.py     # Image normalization, contrast enhancement, dataset prep
│   ├── object_detection_pipeline.py     # Edge detection and spatial zone mapping
│   └── voice_guidance_synthesizer.py    # Priority auditory guidance generation
├── data/
│   └── samples/                         # Sample test frames and annotations
├── reports/
│   └── hackathon_prototype_architecture.md # System architecture, latency, and hardware specs
└── README.md                            # Hackathon documentation
```

---

## 👤 Author
**Kunisetty Giridhar Sai**  
- Email: [kunisettygiridharsai@gmail.com](mailto:kunisettygiridharsai@gmail.com)  
- LinkedIn: [linkedin.com/in/kunisetty-giridhar-sai](https://linkedin.com/in/kunisetty-giridhar-sai)  
- GitHub: [github.com/KUNISETTY-GIRIDHAR-SAI](https://github.com/KUNISETTY-GIRIDHAR-SAI)
