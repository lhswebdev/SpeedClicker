<script>
  import { createEventDispatcher } from 'svelte';
  import { gameState, lastScore } from './store.js';
  import ClickGamePlay from './ClickGamePlay.svelte';

  export let disabled = false;

  // whether it's clicked
  let clicked = false;

  const GameState = {
    START: 0,
    PLAYING: 1,
    FINISHED: 2
  };

  gameState.set(GameState.START);

  const changeTo = state => () => {
    if (clicked) return;
    clicked = true;
    setTimeout(() => {
      clicked = false;
      gameState.set(state);
    }, 200);
  };

  const finishGame = score => {
    lastScore.set(score);
    disabled = true;
    gameState.set(GameState.FINISHED);

    // re-enable button after 1 s
    setTimeout(() => disabled = false, 1000);
  };
</script>

<div>
  {#if $gameState == GameState.START}
    <button {disabled} class:clicked on:click={changeTo(GameState.PLAYING)}>
      Click to play
    </button>
  {:else if $gameState == GameState.PLAYING}
    <ClickGamePlay on:finish={e => finishGame(e.detail.amountClicked)} />
  {:else}
    <div>
      <button
        class:clicked
        {disabled}
        on:click={changeTo(GameState.PLAYING)}
      >
        Play again
      </button>
    </div>
  {/if}
</div>

<style>
  div :global(button) {
    width: 20rem;
    height: 5rem;
  }

  button {
    position: relative;
    z-index: 1;
  }

  button::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;

    /* Begin square moving animation */
    width: 20rem;
    height: 5rem;
    background-color: #02b1f7;
    /* End square moving animation */
    
    /*
    width: 0;
    height: 0;
    border-top: 2.5rem solid transparent;
    border-bottom: 2.5rem solid transparent;
    border-left: 20rem solid #02b1f7;
    */
    z-index: -1;
    transition: transform 200ms ease-in;
    transform: scaleX(0);
    transform-origin: right;
  }

  button:not([disabled]):hover::after {
    transform: scaleX(1);
    transform-origin: left;
  }

  button.clicked::after {
    transform: scaleX(0) !important;
    transform-origin: right !important;
  }
</style>
