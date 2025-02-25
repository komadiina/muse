## MUSE
MUSE (*Music Unraveled: Song Exploration*) is a webapp that allows users to explore melodic puzzles in the form of
songs. Inspired by the popular game [Heardle](https://www.heardle.com/), MUSE allows users to listen to a song and
guess the title of the song. The app uses a [YouTube API](https://developers.google.com/youtube/v3/getting-started)
to fetch song details, and additional Python scripts to parse/process the fetched data.

The app is built with [Angular.js](https://angular.dev/), alongside libraries such as [Flowbite](https://flowbite.com/).

#### Features
The app is still undergoing heavy development, therefore it is not production-ready yet.

#### Roadmap
- Add daily puzzles
- Implement core puzzle mechanisms:
  - A predefined and a user interaction-based difficulty scaling
  - Step-by-step hints
- Implement social aspects:
  - User profiles
  - Leaderboards (daily, categorical and overall)
  - Comments
- Better UI/UX because i can't design lmao
- Deployment (containerizing & CI/CD)
