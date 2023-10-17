<template>
  <button class="absolute top-0 right-0 mt-10 mr-10 p-3 rounded-full font-bold text-white bg-[#ECD71A]/[.12]" @click="toggleOnOff">
    <span v-if="isOn">
          <img src="../assets/brain.svg" alt="Brain Icon" class="h-6 w-6" />
        </span>
        <span v-else>
          <img src="../assets/brain.fill.svg" alt="Brain Icon" class="h-6 w-6" />
        </span>
        <span :class="{ 'text-[#ECD71A]': !isOn }"></span>
      </button>
        <div class="flex justify-center items-center">
        <img src="@/assets/WILWIN.svg" alt="WILWIN Logo" class=" mb-44 mt-10 h-11" />
      </div>
      
  
    <div class="flex justify-center items-center font-semibold">
  
      
      <div class="mr-32 mb-32 text-center">
        <select class="mb-10 text-2xl uppercase rounded-full text-[#ECD71A] bg-[#ECD71A]/[.12]" style="font-family: 'SF Mono Medium'" v-model="team1.name">
          <option value="" disabled selected>Select a team</option>
          <option value="Argentina">Argentina</option>
          <option value="Australia">Australia</option>
          <option value="England">England</option>
          <option value="France">France</option>
          <option value="Ireland">Ireland</option>
          <option value="Italy">Italy</option>
          <option value="New Zealand">New Zealand</option>
          <option value="Scotland">Scotland</option>
          <option value="South Africa">South Africa</option>
          <option value="Wales">Wales</option>
        </select>
        <p class="score text-7xl font-black text-[#EEEEEE]">{{ team1.score }}</p>
        <p class="score mt-4 text-sm font-light text-[#EEEEEE]/[.32]" style="font-family: 'SF Mono Light'">BASÉ SUR {{ team1.matchesCount }} MATCHS</p>
        <p class="score mt-0.5 text-sm font-light text-[#EEEEEE]/[.32]" style="font-family: 'SF Mono Light'">COTES A INTEGRER</p>
      </div>
  
  
      <div class="flex justify-center items-center">
        <button @click="calculateWinRate" id=whowilwin_btn class="bg-[#ECD71A] text-[#3B3D33] hover:bg-[#3B3D33] hover:text-[#ECD71A] font-black text-center px-6 py-3 mb-10 rounded-2xl flex flex-col items-center aspect-w-1 aspect-h-1">
          <svg class="mb-1.5" width="45" height="45" viewBox="0 0 76 76" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8.14258 13.211C8.14258 26.3477 14.4406 34.5542 27.0047 38.4028C28.9768 40.8204 31.2034 42.7606 33.3664 44.1283V57.9649H28.3725C23.8876 57.9649 21.5656 60.5413 21.5656 64.7718V70.0202C21.5656 71.4514 22.6789 72.4375 24.0148 72.4375H54.4868C55.8228 72.4375 56.9362 71.4514 56.9362 70.0202V64.7718C56.9362 60.5413 54.5824 57.9649 50.0973 57.9649H45.1353V44.1283C47.2983 42.7606 49.5248 40.8204 51.465 38.4028C64.0612 34.5542 70.3592 26.3477 70.3592 13.211C70.3592 9.93473 68.3234 7.93083 64.92 7.93083H58.7491C58.2401 4.68639 55.9501 2.71429 52.1012 2.71429H26.4004C22.5834 2.71429 20.2614 4.65459 19.7525 7.93083H13.5818C10.1783 7.93083 8.14258 9.93473 8.14258 13.211ZM12.6911 13.6563C12.6911 13.1473 13.0728 12.7338 13.6135 12.7338H19.5935V18.9682C19.5935 23.8348 20.8658 28.3516 22.8379 32.2639C16.19 28.8923 12.6911 22.7215 12.6911 13.6563ZM55.632 32.2639C57.6359 28.3516 58.9081 23.8348 58.9081 18.9682V12.7338H64.888C65.4289 12.7338 65.8106 13.1473 65.8106 13.6563C65.8106 22.7215 62.3116 28.8923 55.632 32.2639Z" fill="#3B3D33"/>
          </svg>
          WHO WILWIN ?
        </button>
      </div>
  
  
      <div class="ml-32 mb-32 text-center">
        <select class="mb-10 text-2xl uppercase rounded-full text-[#ECD71A] bg-[#ECD71A]/[.12]" style="font-family: 'SF Mono Medium'" v-model="team2.name">
          <option value="" disabled selected>Select a team</option>
          <option value="Argentina">Argentina</option>
          <option value="Australia">Australia</option>
          <option value="England">England</option>
          <option value="France">France</option>
          <option value="Ireland">Ireland</option>
          <option value="Italy">Italy</option>
          <option value="New Zealand">New Zealand</option>
          <option value="Scotland">Scotland</option>
          <option value="South Africa">South Africa</option>
          <option value="Wales">Wales</option>
        </select>
        <p class="score text-7xl font-black text-[#EEEEEE]">{{ team2.score }}</p>
        <p class="score mt-4 text-sm font-light text-[#EEEEEE]/[.32]" style="font-family: 'SF Mono Light'">BASÉ SUR {{ team2.matchesCount }} MATCHS</p>
        <p class="score mt-0.5 text-sm font-light text-[#EEEEEE]/[.32]" style="font-family: 'SF Mono Light'">COTES A INTEGRER</p>
      </div>
    </div>
  
    
    <div class="flex justify-center text-[#EEEEEE] text-lg font-bold mt-20">
      <div class="text-center mx-16">
        <div class="flex flex-col items-center">
          <label for="input1">Intempéries</label>
          <input type="checkbox" v-model="weatherFilter" class="cursor-pointer h-10 w-10 bg-[#ECD71A]/[.12] mt-4 rounded-md checked:bg-[#ECD71A]" id="input1"/>
        </div>
      </div>
      <div class="text-center mx-16">
        <div class="flex flex-col items-center">
          <label for="input2">Température</label>
          <select v-model="temperatureFilter" class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center" id="input2">
            <option value="0" selected>Désactivé</option>
            <optgroup label="Options">
            <option value="Cold">Froid</option>
            <option value="Medium">Tempéré</option>
            <option value="Hot">Chaud</option>
            </optgroup>
          </select>
        </div>
      </div>
      <div class="text-center mx-16">
        <div class="flex flex-col items-center">
          <label for="input3">Vent</label>
          <select v-model="windFilter" class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center" id="input3">
            <option value="0" selected>Désactivé</option>
            <optgroup label="Options">
            <option value="Light">Vent faible</option>
            <option value="Medium">Vent modéré</option>
            <option value="Strong">Vent fort</option>
            </optgroup>
          </select>
        </div>
      </div>
      <div class="text-center mx-16">
        <div class="flex flex-col items-center">
          <label for="input4">Pression</label>
          <select v-model="pressureFilter" class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center" id="input4">
            <option value="0" selected>Désactivé</option>
            <optgroup label="Options">
              <option value="Low">Basse pression</option>
              <option value="Medium">Pression moyenne</option>
              <option value="High">Haute pression</option>
            </optgroup>
          </select>
        </div>
      </div>
    </div>
  </template>
  
  <style>
  
  .score {
    font-family: 'SF Pro Rounded';
  }
  
  input {
    -webkit-appearance: none;
  }
  
  select {
    -webkit-appearance: none;
    text-align-last: center;
    padding: 0.5rem 1rem;
    box-sizing: border-box;
    cursor: pointer;
    text-transform: uppercase;
    font-family: SF Mono Light;
    font-size :medium;
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
  
  import axios from 'axios'
  
  export default {
    data() {
      return {
          team1: {
            name: '',
            score: 0,
            matchesCount: 0
          },
          team2: {
            name: '',
            score: 0,
            matchesCount: 0
          },
          isOn: true,
          apiError: false,
          apiResponse: null,  // to store the API response
          // Adding new data properties for the additional parameters
          _weatherFilter: false,
          temperatureFilter: 0,
          windFilter: 0,
          pressureFilter: 0,
          dfPath: '../API-&-scripts/merged_weather_rugby_final.csv'  // Adjust the path as needed
        };
    },
    computed: {
      weatherFilter: {
        get() {
          return this._weatherFilter ? 'True' : 'False';
        },
        set(value) {
          this._weatherFilter = value === 'True' || value === true;
        }
      }
    },
    methods: {
      toggleOnOff() {
          this.isOn = !this.isOn;
      },
      async calculateWinRate() {
  try {
    // Make the API request with the new parameters
    const response = await axios.post('http://127.0.0.1:5000/api/calculate_win_rate', {
      home_team: this.team1.name,
      away_team: this.team2.name,
      weather_filter: this.weatherFilter,
      temperature_filter: this.temperatureFilter,
      wind_filter: this.windFilter,
      pressure_filter: this.pressureFilter,
      df_path: this.dfPath
    });

    // Log the API response to the console
    console.log('API Response:', response.data);

    // Store the API response
    this.apiResponse = response.data;

    // Update the teams' scores with the data from the API response
    if (response.data.status === 'Success') {
      const teams = response.data.teams;
      this.team1.score = teams[this.team1.name].wilwin_score;
      this.team2.score = teams[this.team2.name].wilwin_score;

      // Update the "BASÉ SUR X MATCHS" text for each team
      this.team1.matchesCount = teams[this.team1.name].method2.matches_count;
      this.team2.matchesCount = teams[this.team2.name].method2.matches_count;
    }
  } catch (error) {
    console.error('Error during the API request:', error);
    this.apiResponse = 'Error retrieving data';
    this.team1.score = 'No data';
    this.team2.score = 'No data';
  }
}
  }
    
  }
  </script>