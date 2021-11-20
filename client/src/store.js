import { derived, get, readable, writable } from 'svelte/store';

/** @typedef {{ name: string, score: number, time: number }} LeaderboardEntry */

export const gameState = writable(0);
export const lastScore = writable(/** @type {number | null} */ (null));
export const username = writable('');
export const displayName = derived(username, $name => $name || 'Anonymous');

export const highscore = derived(lastScore, $lastScore =>
  $lastScore != null ? Math.max(get(highscore), $lastScore) : null
);

export const leaderboard = readable(/** @type {LeaderboardEntry[]} */ ([]), set => {
  const interval = setInterval(() => {
    // fetch leaderboard and set store
    fetch('http://127.0.0.1:8000/leaderboard')
      .then(response => response.json())
      .then(data => set(data));
  }, 10 * 1000);
  set([{
    name: 'anon',
    score: 69,
    time: Date.now(),
  }]);
  return () => clearInterval(interval);
});

highscore.subscribe($highscore => {
  if ($highscore == null) return;
  const result = { highscore: $highscore, name: get(displayName) };
  // FIXME replace with actual fetch call
  fetch('http://clicker.sagg.in:8003/highscore', {method: 'POST', headers: {'Content-Type': 'application/json',},body: JSON.stringify(result)})
  console.log('UPLOADING TO SERVER:', result);
});
