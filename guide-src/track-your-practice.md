---
{
 "slug": "track-your-practice",
 "h1": "Track your practice",
 "seo_title": "Track Practice Time, Goals and Streaks | Music Folder",
 "description": "See how Music Folder counts practice time, set a daily practice goal and reminder, and review your week, month and year and your most practiced pieces.",
 "intent": "general",
 "intent_note": "Students, teachers and adult learners who want a practice log and daily goal without a separate app, and users wondering how practice minutes are counted.",
 "searches": ["practice log", "practice timer", "practice goal", "daily goal", "streak", "reminder", "notification", "practice history", "minutes practiced", "most practiced"],
 "availability": [],
 "related": ["use-the-metronome", "play-along-with-recordings", "back-up-and-restore-your-library"],
 "feature_link": {"href": "/for/students", "text": "Music Folder for students"},
 "documents": ["App/GoalsView.swift", "App/PracticeInsightsViews.swift", "App/HomePracticeCard.swift", "App/GoalAdjustSheet.swift", "App/GoalOffer.swift", "App/AccountView.swift", "Data/PracticeSessionTracker.swift", "Services/PracticePeriodSummary.swift", "Services/PracticeInsights.swift", "R48"],
 "verified": "76048e78",
 "differs_from_4_2": null,
 "shots": [
  {"id": "practice-screen", "kind": "screen", "device": "ipad", "orientation": "portrait", "state": "The Practice screen on iPad in portrait, opened from Home's Practice card: the Today card with Change Goal (29 min of 30, 14-day streak), Week selected, this week's card with the total, the comparison line, the bar chart with the dotted goal line, Average per practice day and Goal reached, and Most Practiced with four pieces and See All.", "alt": "The Practice screen: today's minutes against a 30-minute goal, a weekly bar chart with a dotted goal line, and a Most Practiced list of four pieces.", "caption": null, "reuse": "practice-ipad.jpg"}
 ],
 "open_questions": []
}
---
Music Folder keeps a practice log for you without a timer to start or stop. It counts the time you spend with your music open, shows it against a daily goal, and keeps a streak of the days you played.

## How practice time is counted

Practice time is the time a piece is open in the reader: a piece from your library, a set list or a Planning Center plan. These rules decide what counts:

- A visit counts once it reaches one minute. Opening a score to check something doesn't add time.
- Only time with the app on screen counts.
- If 15 minutes pass without a touch, a pencil stroke or a page turn, counting stops until you're back. A running metronome, a playing recording, the tuner or the recorder keeps it going, so playing along without touching the screen still counts.
- In a set list, each piece gets the time it was on screen.

Your practice history is personal. It's never shared with collaborators, and it's included in your library backups.

## Set a daily goal

1. On Home, tap **Set Goal** in the Practice card. If you already have a goal, touch and hold the card and choose **Edit Daily Goal**.
2. Pick one of the quick choices (10, 15, 30, 45 or 60 minutes), or tap − and + to change it in 5-minute steps, from 5 minutes to 3 hours a day.
3. Tap {sf:checkmark} **Save Goal**.

You can also change the goal with **Change Goal** on the Practice screen, or in Account under **Practice › Practice Goal**. To open Account, tap your picture or initials at the top of Home. Where the app shows a sidebar (iPad and Mac in a full-size window, with iPadOS 18 or later), Account is your name at the bottom of the sidebar instead.

Your streak grows on every day you practice, even if you don't reach the goal that day.

Note: If you haven't set a goal, Home's Practice card offers one after your first counted session, for example "You played 12 minutes today. Set a daily goal?" Choosing a goal there is followed by an offer to remind you at about the time you just practiced. **Not Now** closes the offer for good.

## Get a daily reminder

In the **Daily Goal** sheet, turn on **Daily reminder** and set the time with **Remind me at**.

For more control, open Account and choose **Practice › Reminders**. Turn on **Daily Practice Reminder**, set the **Time**, and under **Repeat** choose **Daily**, **Weekdays only** or the days you want. Your changes take effect when you tap **Done** or go back.

The first time you turn a reminder on, the app asks permission to send notifications: right away in the Daily Goal sheet, when you leave the Reminders screen, or when you tap **Turn On** in Home's reminder offer. If you don't allow notifications, the reminder switches back off.

## See your practice

The Practice card on Home shows today's minutes against your goal, your streak and the current week. Tap the card to open the **Practice** screen.

{shot:practice-screen}

- **Today** shows the minutes you've played, how far you are from your goal and your streak.
- **Week**, **Month** and **Year** switch the card below between periods. Tap the arrows on the card to look at earlier ones.
- The card shows the total for the period, how it compares with the one before, and a bar chart with your goal as a dotted line. Tap a bar to see that day's (or month's) time. **Average per practice day** counts only the days you played; **Goal reached** counts the days you met your goal.
- **Most Practiced** ranks the pieces you spent the most time on in the same period. Tap a piece to open it, or **See All** for the full list.

Time that isn't tied to a piece in your library, such as set-list pages, Planning Center songs in a set list or pieces you've since deleted, appears in one line, **Not linked to a piece**.

Weeks start on the first day of the week for your region. To share your streak or a milestone as an image, tap {sf:square.and.arrow.up} at the top of the Practice screen.
