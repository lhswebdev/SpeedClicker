<script>
  import { createEventDispatcher, onDestroy, onMount } from 'svelte';

  export let gameTime = 1;

  const dispatch = createEventDispatcher();

  let amountClicked = 0;
  let timeLeft = gameTime;
  let interval;
  let timeout;

  onMount(() => timeout = setTimeout(() => {
    dispatch('finish', { amountClicked });
  }, gameTime * 1000));
  onDestroy(() => clearTimeout(timeout));

  onMount(() => interval = setInterval(() => {
    timeLeft -= .01;
  }, 10));
  onDestroy(() => clearInterval(interval));
</script>

<div>
  <button on:click={() => amountClicked++}>
    Clicked: {amountClicked}
  </button>
  <p>You have {timeLeft.toFixed(2)}s left</p>
</div>
