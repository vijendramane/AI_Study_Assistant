# 🎓 AI Study Assistant - Exam Revision Helper

A comprehensive Python application to help students organize, track, and revise their exam syllabus effectively.

## Features

### 📚 **Subject Management**
- Add multiple subjects with exam dates and priorities
- Edit existing subjects
- Set priority levels (high/medium/low)
- Add general notes for each subject

### 📝 **Topic Organization**
- Add topics for each subject
- Track completion status (not started/in progress/completed)
- Rate confidence level (1-10 scale)
- Add personal notes for each topic

### 📊 **Progress Tracking**
- Visual progress bars for each subject
- Real-time completion statistics
- Track study sessions and dates
- Monitor confidence levels across topics

### 🎯 **Interactive Revision Sessions**
- Guided study sessions
- Update topic status and confidence
- Add notes during revision
- Smart topic recommendations based on completion and confidence

### ❓ **Quiz Mode**
- Random topic selection
- Self-assessment scoring
- Automatic progress updates
- Performance feedback

### 📅 **Smart Study Scheduling**
- Exam date-based planning
- Priority-based recommendations
- Calculate topics per day needed
- Workload warnings for heavy schedules

### 💡 **AI Study Tips**
- Personalized tips based on progress
- Evidence-based study techniques
- Motivation and productivity advice
- Adaptive recommendations

### 📈 **Detailed Statistics**
- Overall completion rates
- Subject-wise breakdowns
- Confidence analytics
- Study session tracking

## How to Use

### 1. **Run the Application**
```bash
python study_assistant.py
```

### 2. **First-Time Setup**
1. Choose option 1 to add your first subject
2. Enter subject name, exam date, and priority
3. Choose option 2 to add topics to your subject
4. Start studying!

### 3. **Daily Workflow**
1. Check progress (option 3)
2. Start revision session (option 4) or quiz mode (option 5)
3. Update confidence levels and add notes
4. Review study schedule (option 6)

### 4. **Study Tips Integration**
- Use option 7 to get personalized study tips
- View statistics (option 8) to track improvement
- Adjust study schedule based on recommendations

## Example Usage

### Adding a Subject
```
Subject: Mathematics
Exam Date: 2024-01-15
Priority: high
Notes: Focus on calculus and algebra
```

### Adding Topics
```
Topics:
- Differential Calculus
- Integral Calculus
- Linear Algebra
- Probability
- Statistics
```

### Revision Session
- Review each topic
- Rate understanding (1-10)
- Add study notes
- Update completion status

## Data Storage

All your study data is automatically saved to `study_data.json` in the same directory. This ensures your progress is preserved between sessions.

## Tips for Effective Use

1. **Be Honest with Confidence Ratings** - This helps the AI recommend the right topics for revision
2. **Regular Updates** - Update your progress after each study session
3. **Use Notes Feature** - Add key insights and difficult concepts
4. **Follow Schedule Recommendations** - The AI calculates optimal study pace
5. **Take Advantage of Quiz Mode** - Great for quick self-assessment

## Study Methodologies Supported

- **Spaced Repetition** - Topics with low confidence are prioritized
- **Active Recall** - Quiz mode encourages self-testing
- **Progress Tracking** - Visual feedback maintains motivation
- **Goal Setting** - Exam dates create deadline-driven planning

## Requirements

- Python 3.6+
- No additional packages required (uses standard library only)

## Getting Started

Simply run:
```bash
python study_assistant.py
```

Follow the interactive menu to set up your subjects and start studying smarter!

---

**Good luck with your exams! 🌟**

