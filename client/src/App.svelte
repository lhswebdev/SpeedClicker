<script>
  import { gameState, highscore, lastScore, username } from './store.js';
  import ClickGame from './ClickGame.svelte';
  import Leaderboard from './Leaderboard.svelte';
</script>

<svelte:head>
  <title>Speed Clicker</title>
</svelte:head>

<main>
  <h1>Speed Clicker</h1>
  <div class="two-col">
    <div class="col">
      <div class="info">
        <div class="username-input">
          <label for="username">Username</label>
          <input
            name="username"
            placeholder="Enter username..."
            disabled={$gameState}
            bind:value={$username}
          />
        </div>
        <span>Last score: {$lastScore ?? 'n/a'}</span>
        <span>Highscore: {$highscore ?? 'n/a'}</span>
      </div>
      <ClickGame disabled={!$username} />
    </div>
    <div class="col">
      <Leaderboard />
    </div>
  </div>
</main>

<style>
  .info {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem;
  }

  .two-col {
    display: flex;
    flex-direction: row;
    gap: 3rem;
  }
</style>
