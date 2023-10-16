<template>
      <div class="flex justify-center items-center">
      <img src="@/assets/WILWIN.svg" alt="WILWIN Logo" class=" mb-44 mt-10 h-11" />
    </div>
  <div class="flex justify-center items-center font-semibold">
    <div class="mr-32 mb-32 text-center text-4xl">
      <button class="mb-10 px-4 py-1 uppercase rounded-full text-[#ECD71A] bg-[#ECD71A]/[.12] flex justify-center items-center">{{ team1.name }}
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="ml-3 w-7 h-7">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
        </svg>
      </button>
      <p class="text-7xl font-black text-[#EEEEEE]">{{ team1.score }}</p>
    </div>
    <div class="flex justify-center items-center">
      <button class="bg-[#ECD71A] text-[#3B3D33] hover:bg-[#3B3D33] hover:text-[#ECD71A] font-black text-center px-6 py-3 mb-8 rounded-2xl flex flex-col items-center aspect-w-1 aspect-h-1">
        <svg class="mb-1.5" width="45" height="45" viewBox="0 0 76 76" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8.14258 13.211C8.14258 26.3477 14.4406 34.5542 27.0047 38.4028C28.9768 40.8204 31.2034 42.7606 33.3664 44.1283V57.9649H28.3725C23.8876 57.9649 21.5656 60.5413 21.5656 64.7718V70.0202C21.5656 71.4514 22.6789 72.4375 24.0148 72.4375H54.4868C55.8228 72.4375 56.9362 71.4514 56.9362 70.0202V64.7718C56.9362 60.5413 54.5824 57.9649 50.0973 57.9649H45.1353V44.1283C47.2983 42.7606 49.5248 40.8204 51.465 38.4028C64.0612 34.5542 70.3592 26.3477 70.3592 13.211C70.3592 9.93473 68.3234 7.93083 64.92 7.93083H58.7491C58.2401 4.68639 55.9501 2.71429 52.1012 2.71429H26.4004C22.5834 2.71429 20.2614 4.65459 19.7525 7.93083H13.5818C10.1783 7.93083 8.14258 9.93473 8.14258 13.211ZM12.6911 13.6563C12.6911 13.1473 13.0728 12.7338 13.6135 12.7338H19.5935V18.9682C19.5935 23.8348 20.8658 28.3516 22.8379 32.2639C16.19 28.8923 12.6911 22.7215 12.6911 13.6563ZM55.632 32.2639C57.6359 28.3516 58.9081 23.8348 58.9081 18.9682V12.7338H64.888C65.4289 12.7338 65.8106 13.1473 65.8106 13.6563C65.8106 22.7215 62.3116 28.8923 55.632 32.2639Z" fill="#3B3D33"/>
        </svg>
        WHO WILWIN ?
      </button>
    </div>
    <div class="ml-32 mb-32 text-center text-4xl">
      <button class="mb-10 px-4 py-1 uppercase rounded-full text-[#ECD71A] bg-[#ECD71A]/[.12] flex justify-center items-center">{{ team2.name }}
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="3" stroke="currentColor" class="ml-3 w-7 h-7">
        <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5" />
        </svg>
      </button>
      <p class="text-7xl font-black text-[#EEEEEE]">{{ team2.score }}</p>
    </div>
  </div>
  <div class="flex justify-center text-[#EEEEEE] text-lg font-bold mt-20">
    <div class="text-center mx-16">
      <div class="flex flex-col items-center">
        <label for="input1">Intempéries</label>
        <input type="checkbox" class="cursor-pointer h-8 w-8 bg-[#ECD71A]/[.12] mt-4 rounded-md checked:bg-yellow-400" id="input1"/>
      </div>
    </div>
    <div class="text-center mx-16">
      <div class="flex flex-col items-center">
        <label for="input2">Température</label>
        <select class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center" id="input2">
          <option value="0" selected>Désactivé</option>
          <option value="1">Froid</option>
          <option value="2">Tempéré</option>
          <option value="3">Chaud</option>
        </select>
      </div>
    </div>
    <div class="text-center mx-16">
      <div class="flex flex-col items-center">
        <label for="input3">Vent</label>
        <select class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center" id="input3">
          <option value="0" selected>Désactivé</option>
          <option value="1">Vent faible</option>
          <option value="2">Vent modéré</option>
          <option value="3">Vent fort</option>
        </select>
      </div>
    </div>
    <div class="text-center mx-16">
      <div class="flex flex-col items-center">
        <label for="input4">Pression</label>
        <select class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center capitalize" id="input4">
          <option value="0" selected>Désactivé</option>
          <option value="1">Basse pression</option>
          <option value="2">Pression moyenne</option>
          <option value="3">Haute pression</option>
        </select>
      </div>
    </div>
  </div>
</template>

<style>
input {
  -webkit-appearance: none;
}

select {
  -webkit-appearance: none;
  text-align-last: center;
  padding: 0.5rem 1rem;
  box-sizing: border-box;
}

select option:checked {
  background-color: #ECD71A;
  color: #3B3D33;
}

button {
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
}

button:hover svg path {
  fill: #ECD71A;
}

button:hover {
  background-color: #3B3D33;
  color: #ECD71A;
}

input[type='range']::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 30px;
  width: 30px;
  border-radius: 100%;
  background-color: #ECD71A;
  cursor: pointer;
}
</style>

<script>
export default {
  data() {
    return {
      team1: {
        name: 'Team 1',
        score: '32%'
      },
      team2: {
        name: 'Team 2',
        score: '68%'
      },
    }
  }
}
</script>