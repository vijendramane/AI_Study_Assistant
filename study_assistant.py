import json
import os
import datetime
import random
from typing import Dict, List, Any
   
class StudyAssistant: 
    def __init__(self): 
        self.data_file = "study_data.json"
        self.subjects = self.load_data()  
        
    def load_data(self) -> Dict[str, Any]:
        """Load study data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}
    
    def save_data(self):
        """Save study data to JSON file"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.subjects, f, indent=2, ensure_ascii=False)
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("🎓 AI STUDY ASSISTANT - EXAM REVISION HELPER")
        print("="*50)
        print("1. 📚 Add/Edit Subject")
        print("2. 📝 Add Topics to Subject")
        print("3. 📊 View Study Progress")
        print("4. 🎯 Start Revision Session")
        print("5. ❓ Quiz Mode")
        print("6. 📅 Set Study Schedule")
        print("7. 💡 Get Study Tips")
        print("8. 📈 View Statistics")
        print("9. 🗑️  Delete Subject/Topic")
        print("10. 🚪 Exit")
        print("="*50)
    
    def add_subject(self):
        """Add or edit a subject"""
        print("\n📚 SUBJECT MANAGEMENT")
        print("-" * 30) 
        
        if self.subjects:
            print("Existing subjects:")
            for i, subject in enumerate(self.subjects.keys(), 1):
                print(f"{i}. {subject}")
            print()
        
        subject_name = input("Enter subject name: ").strip()
        if not subject_name:
            print("❌ Subject name cannot be empty!")
            return
        
        if subject_name not in self.subjects:
            self.subjects[subject_name] = {
                "topics": {},
                "exam_date": "",
                "priority": "medium",
                "total_sessions": 0,
                "last_studied": "",
                "notes": ""
            }
            print(f"✅ Subject '{subject_name}' added successfully!")
        else:
            print(f"📝 Editing existing subject '{subject_name}'")
        
        # Get additional details
        exam_date = input("Enter exam date (YYYY-MM-DD) [optional]: ").strip()
        if exam_date:
            try: 
                datetime.datetime.strptime(exam_date, "%Y-%m-%d")
                self.subjects[subject_name]["exam_date"] = exam_date
            except ValueError:
                print("⚠️ Invalid date format, skipping...")
        
        priority = input("Enter priority (high/medium/low) [medium]: ").strip().lower()
        if priority in ["high", "medium", "low"]:
            self.subjects[subject_name]["priority"] = priority
        
        notes = input("Enter general notes [optional]: ").strip()
        if notes:
            self.subjects[subject_name]["notes"] = notes
        
        self.save_data()
        print("💾 Data saved successfully!")
    
    def add_topics(self):
        """Add topics to a subject"""
        if not self.subjects:
            print("❌ No subjects found! Please add a subject first.")
            return
        
        print("\n📝 ADD TOPICS")
        print("-" * 20)
        
        # Display subjects
        subjects_list = list(self.subjects.keys())
        for i, subject in enumerate(subjects_list, 1):
            print(f"{i}. {subject}")
        
        try:
            choice = int(input("\nSelect subject number: ")) - 1
            if 0 <= choice < len(subjects_list):
                subject_name = subjects_list[choice]
            else:
                print("❌ Invalid selection!")
                return
        except ValueError:
            print("❌ Please enter a valid number!")
            return
        
        print(f"\nAdding topics to: {subject_name}")
        print("Enter topics one by one (press Enter with empty line to finish):")
        
        while True:
            topic = input("Topic: ").strip()
            if not topic:
                break
            
            if topic not in self.subjects[subject_name]["topics"]:
                self.subjects[subject_name]["topics"][topic] = {
                    "status": "not_started",  # not_started, in_progress, completed
                    "confidence": 0,  # 0-10 scale
                    "study_time": 0,  # minutes
                    "last_reviewed": "",
                    "notes": "",
                    "difficulty": "medium"
                }
                print(f"✅ Added: {topic}")
            else:
                print(f"⚠️ Topic '{topic}' already exists!")
        
        self.save_data()
        print("💾 Topics saved successfully!")
    
    def view_progress(self):
        """View study progress for all subjects"""
        if not self.subjects:
            print("❌ No subjects found!")
            return
        
        print("\n📊 STUDY PROGRESS OVERVIEW")
        print("=" * 50)
        
        for subject_name, subject_data in self.subjects.items():
            print(f"\n📚 {subject_name.upper()}")
            print(f"Priority: {subject_data['priority'].upper()}")
            if subject_data['exam_date']:
                exam_date = datetime.datetime.strptime(subject_data['exam_date'], "%Y-%m-%d")
                days_left = (exam_date - datetime.datetime.now()).days
                print(f"Exam Date: {subject_data['exam_date']} ({days_left} days left)")
            
            topics = subject_data["topics"]
            if not topics:
                print("No topics added yet.")
                continue
            
            # Calculate progress
            total_topics = len(topics)
            completed = sum(1 for t in topics.values() if t["status"] == "completed")
            in_progress = sum(1 for t in topics.values() if t["status"] == "in_progress")
            
            print(f"Progress: {completed}/{total_topics} completed, {in_progress} in progress")
            
            # Progress bar
            progress_percent = (completed / total_topics) * 100
            bar_length = 20
            filled_length = int(bar_length * progress_percent // 100)
            bar = "█" * filled_length + "-" * (bar_length - filled_length)
            print(f"[{bar}] {progress_percent:.1f}%")
            
            # Show topic details
            print("\nTopics:")
            for topic, data in topics.items():
                status_emoji = {"not_started": "🔴", "in_progress": "🟡", "completed": "🟢"}
                confidence_bar = "⭐" * data["confidence"]
                print(f"  {status_emoji[data['status']]} {topic} - Confidence: {confidence_bar}")
    
    def start_revision(self):
        """Start interactive revision session"""
        if not self.subjects:
            print("❌ No subjects found!")
            return
        
        print("\n🎯 REVISION SESSION")
        print("-" * 25)
        
        # Select subject
        subjects_list = list(self.subjects.keys())
        for i, subject in enumerate(subjects_list, 1):
            print(f"{i}. {subject}")
        
        try:
            choice = int(input("\nSelect subject: ")) - 1
            subject_name = subjects_list[choice]
        except (ValueError, IndexError):
            print("❌ Invalid selection!")
            return
        
        topics = self.subjects[subject_name]["topics"]
        if not topics:
            print("❌ No topics found for this subject!")
            return
        
        # Filter topics that need revision
        revision_topics = [t for t, data in topics.items() 
                          if data["status"] != "completed" or data["confidence"] < 7]
        
        if not revision_topics:
            print("🎉 All topics are well-understood! Great job!")
            return
        
        print(f"\nStarting revision for: {subject_name}")
        print(f"Topics to review: {len(revision_topics)}")
        
        for topic in revision_topics:
            print(f"\n📖 Studying: {topic}")
            print(f"Current status: {topics[topic]['status']}")
            print(f"Confidence level: {topics[topic]['confidence']}/10")
            
            if topics[topic]['notes']:
                print(f"Notes: {topics[topic]['notes']}")
            
            # Interactive session
            print("\nWhat would you like to do?")
            print("1. Mark as completed")
            print("2. Update confidence level")
            print("3. Add notes")
            print("4. Skip to next topic")
            print("5. End session")
            
            action = input("Choose action (1-5): ").strip()
            
            if action == "1":
                topics[topic]["status"] = "completed"
                topics[topic]["last_reviewed"] = datetime.datetime.now().strftime("%Y-%m-%d")
                print("✅ Topic marked as completed!")
            
            elif action == "2":
                try:
                    confidence = int(input("Enter confidence level (1-10): "))
                    if 1 <= confidence <= 10:
                        topics[topic]["confidence"] = confidence
                        topics[topic]["status"] = "completed" if confidence >= 8 else "in_progress"
                        print(f"✅ Confidence updated to {confidence}/10")
                    else:
                        print("❌ Please enter a number between 1-10")
                except ValueError:
                    print("❌ Please enter a valid number")
            
            elif action == "3":
                note = input("Enter your notes: ").strip()
                topics[topic]["notes"] = note
                print("✅ Notes added!")
            
            elif action == "4":
                continue
            
            elif action == "5":
                break
            
            # Update last studied
            self.subjects[subject_name]["last_studied"] = datetime.datetime.now().strftime("%Y-%m-%d")
            self.subjects[subject_name]["total_sessions"] += 1
        
        self.save_data()
        print("💾 Session saved! Great work! 🎉")
    
    def quiz_mode(self):
        """Interactive quiz mode"""
        if not self.subjects:
            print("❌ No subjects found!")
            return
        
        print("\n❓ QUIZ MODE")
        print("-" * 15)
        
        # Select subject
        subjects_list = list(self.subjects.keys())
        for i, subject in enumerate(subjects_list, 1):
            print(f"{i}. {subject}")
        
        try:
            choice = int(input("\nSelect subject: ")) - 1
            subject_name = subjects_list[choice]
        except (ValueError, IndexError):
            print("❌ Invalid selection!")
            return
        
        topics = list(self.subjects[subject_name]["topics"].keys())
        if not topics:
            print("❌ No topics found for this subject!")
            return
        
        print(f"\n🎯 Quiz on: {subject_name}")
        print("I'll ask you about random topics. Rate your understanding!")
        
        score = 0
        total_questions = min(5, len(topics))
        
        for i in range(total_questions):
            topic = random.choice(topics)
            print(f"\nQuestion {i+1}: Explain '{topic}'")
            
            input("Press Enter when you've thought about it...")
            
            understanding = input("How well do you understand this topic? (1-10): ").strip()
            try:
                rating = int(understanding)
                if 1 <= rating <= 10:
                    score += rating
                    # Update topic data
                    self.subjects[subject_name]["topics"][topic]["confidence"] = rating
                    if rating >= 8:
                        self.subjects[subject_name]["topics"][topic]["status"] = "completed"
                    elif rating >= 5:
                        self.subjects[subject_name]["topics"][topic]["status"] = "in_progress"
                    
                    print(f"✅ Recorded: {rating}/10")
                else:
                    print("❌ Please enter 1-10")
            except ValueError:
                print("❌ Invalid input")
        
        average_score = score / total_questions
        print(f"\n🏆 Quiz Complete!")
        print(f"Average Score: {average_score:.1f}/10")
        
        if average_score >= 8:
            print("🌟 Excellent! You're well-prepared!")
        elif average_score >= 6:
            print("👍 Good progress! Keep studying!")
        else:
            print("📚 Need more practice! Don't give up!")
        
        self.save_data()
    
    def study_schedule(self):
        """Set study schedule and reminders"""
        print("\n📅 STUDY SCHEDULE")
        print("-" * 20)
        
        if not self.subjects:
            print("❌ No subjects found!")
            return
        
        print("Upcoming exams and recommended study plan:")
        
        # Sort subjects by exam date and priority
        scheduled_subjects = []
        for name, data in self.subjects.items():
            if data["exam_date"]:
                exam_date = datetime.datetime.strptime(data["exam_date"], "%Y-%m-%d")
                days_left = (exam_date - datetime.datetime.now()).days
                scheduled_subjects.append((name, days_left, data["priority"]))
        
        scheduled_subjects.sort(key=lambda x: (x[1], {"high": 1, "medium": 2, "low": 3}[x[2]]))
        
        for subject, days_left, priority in scheduled_subjects:
            topics = self.subjects[subject]["topics"]
            incomplete_topics = [t for t, data in topics.items() 
                               if data["status"] != "completed"]
            
            print(f"\n📚 {subject} ({days_left} days left, {priority} priority)")
            print(f"Topics to complete: {len(incomplete_topics)}")
            
            if incomplete_topics and days_left > 0:
                topics_per_day = len(incomplete_topics) / days_left
                print(f"Recommended: {topics_per_day:.1f} topics per day")
                
                if topics_per_day > 3:
                    print("⚠️ Warning: Heavy study load required!")
                elif topics_per_day > 1:
                    print("📈 Moderate study pace needed")
                else:
                    print("✅ Manageable study pace")
    
    def get_study_tips(self):
        """Provide AI-generated study tips"""
        tips = [
            "🧠 Use the Pomodoro Technique: 25 minutes focused study, 5-minute break",
            "📝 Create mind maps to visualize connections between topics",
            "🔄 Review topics multiple times with increasing intervals (spaced repetition)",
            "📚 Teach concepts to someone else or explain them out loud",
            "🎯 Focus on understanding concepts rather than memorizing facts",
            "💡 Use mnemonics and memory techniques for difficult information",
            "📱 Minimize distractions: put phone away during study sessions",
            "🏃 Take regular breaks and include physical activity",
            "🍎 Maintain good nutrition and stay hydrated",
            "😴 Get adequate sleep - your brain consolidates memory during sleep",
            "📊 Track your progress to stay motivated",
            "🤝 Form study groups for collaborative learning",
            "❓ Ask questions and seek clarification on difficult topics",
            "📝 Make your own notes in your own words",
            "🔍 Use active recall: test yourself without looking at notes"
        ]
        
        print("\n💡 AI STUDY TIPS")
        print("-" * 20)
        
        # Show personalized tips based on user's data
        if self.subjects:
            total_topics = sum(len(subject["topics"]) for subject in self.subjects.values())
            completed_topics = sum(
                sum(1 for topic in subject["topics"].values() if topic["status"] == "completed")
                for subject in self.subjects.values()
            )
            
            if total_topics > 0:
                completion_rate = (completed_topics / total_topics) * 100
                print(f"📊 Your current completion rate: {completion_rate:.1f}%")
                
                if completion_rate < 25:
                    print("🚀 Just getting started! Here are some tips to build momentum:")
                elif completion_rate < 50:
                    print("👍 Good progress! Here are tips to maintain consistency:")
                elif completion_rate < 75:
                    print("💪 You're doing great! Tips for the final push:")
                else:
                    print("🌟 Excellent progress! Tips for exam preparation:")
        
        # Show 3 random tips
        selected_tips = random.sample(tips, 3)
        for i, tip in enumerate(selected_tips, 1):
            print(f"{i}. {tip}")
        
        print("\n🎯 Remember: Consistency is key to success!")
    
    def view_statistics(self):
        """View detailed statistics"""
        if not self.subjects:
            print("❌ No subjects found!")
            return
        
        print("\n📈 STUDY STATISTICS")
        print("=" * 30)
        
        total_subjects = len(self.subjects)
        total_topics = sum(len(subject["topics"]) for subject in self.subjects.values())
        
        completed_topics = sum(
            sum(1 for topic in subject["topics"].values() if topic["status"] == "completed")
            for subject in self.subjects.values()
        )
        
        in_progress_topics = sum(
            sum(1 for topic in subject["topics"].values() if topic["status"] == "in_progress")
            for subject in self.subjects.values()
        )
        
        print(f"📚 Total Subjects: {total_subjects}")
        print(f"📝 Total Topics: {total_topics}")
        print(f"✅ Completed Topics: {completed_topics}")
        print(f"🟡 In Progress Topics: {in_progress_topics}")
        print(f"🔴 Not Started Topics: {total_topics - completed_topics - in_progress_topics}")
        
        if total_topics > 0:
            completion_percentage = (completed_topics / total_topics) * 100
            print(f"📊 Overall Completion: {completion_percentage:.1f}%")
        
        # Subject-wise breakdown
        print("\n📊 Subject-wise Progress:")
        for subject_name, subject_data in self.subjects.items():
            topics = subject_data["topics"]
            if topics:
                completed = sum(1 for t in topics.values() if t["status"] == "completed")
                total = len(topics)
                percentage = (completed / total) * 100
                print(f"  {subject_name}: {completed}/{total} ({percentage:.1f}%)")
        
        # Study streak
        print(f"\n📅 Total Study Sessions: {sum(s['total_sessions'] for s in self.subjects.values())}")
        
        # Confidence analysis
        all_confidences = []
        for subject in self.subjects.values():
            for topic in subject["topics"].values():
                if topic["confidence"] > 0:
                    all_confidences.append(topic["confidence"])
        
        if all_confidences:
            avg_confidence = sum(all_confidences) / len(all_confidences)
            print(f"🎯 Average Confidence: {avg_confidence:.1f}/10")
    
    def delete_data(self):
        """Delete subjects or topics"""
        if not self.subjects:
            print("❌ No subjects found!")
            return
        
        print("\n🗑️ DELETE DATA")
        print("-" * 15)
        print("1. Delete a subject")
        print("2. Delete a topic")
        print("3. Cancel")
        
        choice = input("Choose option (1-3): ").strip()
        
        if choice == "1":
            subjects_list = list(self.subjects.keys())
            for i, subject in enumerate(subjects_list, 1):
                print(f"{i}. {subject}")
            
            try:
                selection = int(input("Select subject to delete: ")) - 1
                subject_name = subjects_list[selection]
                
                confirm = input(f"Are you sure you want to delete '{subject_name}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    del self.subjects[subject_name]
                    self.save_data()
                    print(f"✅ Subject '{subject_name}' deleted!")
                else:
                    print("❌ Deletion cancelled.")
            except (ValueError, IndexError):
                print("❌ Invalid selection!")
        
        elif choice == "2":
            # Similar implementation for deleting topics
            print("Topic deletion functionality - select subject first...")
            # Implementation similar to above
        
        elif choice == "3":
            print("Operation cancelled.")
    
    def run(self):
        """Main application loop"""
        print("🎓 Welcome to AI Study Assistant!")
        print("Your intelligent companion for exam preparation!")
        
        while True:
            try:
                self.display_menu()
                choice = input("\nEnter your choice (1-10): ").strip()
                
                if choice == "1":
                    self.add_subject()
                elif choice == "2":
                    self.add_topics()
                elif choice == "3":
                    self.view_progress()
                elif choice == "4":
                    self.start_revision()
                elif choice == "5":
                    self.quiz_mode()
                elif choice == "6":
                    self.study_schedule()
                elif choice == "7":
                    self.get_study_tips()
                elif choice == "8":
                    self.view_statistics()
                elif choice == "9":
                    self.delete_data()
                elif choice == "10":
                    print("\n🎉 Thanks for using AI Study Assistant!")
                    print("Good luck with your exams! 📚✨")
                    break
                else:
                    print("❌ Invalid choice! Please enter 1-10.")
                
                input("\nPress Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Study hard and succeed!")
                break
            except Exception as e:
                print(f"❌ An error occurred: {e}")
                input("Press Enter to continue...")

if __name__ == "__main__":
    assistant = StudyAssistant()
    assistant.run()




















