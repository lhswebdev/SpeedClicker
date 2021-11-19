<script>
  import { leaderboard } from './store.js';
</script>

<table>
  <tr>
    <th>Place</th>
    <th>Name</th>
    <th>Score</th>
    <th>Time</th>
  </tr>
  {#each $leaderboard.slice(0, 5) as entry, i}
    <tr>
      <td>{i + 1}</td>
      <td>{entry.name}</td>
      <td>{entry.score}</td>
      <td>{new Date(entry.time).toLocaleString()}</td>
    </tr>
  {/each}
</table>

<style>
  table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    padding: .2rem;
  }

  th {
    font-size: 1.5rem;
  }
</style>
