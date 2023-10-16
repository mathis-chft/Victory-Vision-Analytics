<template>
  <div class="scores">
    <div class="team">
      <h2>{{ team1.name }}</h2>
      <p>{{ team1.score }}</p>
    </div>
    <div class="team">
      <h2>{{ team2.name }}</h2>
      <p>{{ team2.score }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      team1: {
        name: 'Team 1',
        score: 0
      },
      team2: {
        name: 'Team 2',
        score: 0
      }
    }
  }
}
</script>

<style>
.scores {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.team {
  margin: 0 20px;
  text-align: center;
}
</style>
