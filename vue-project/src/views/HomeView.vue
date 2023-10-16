<template>
  <button
    class="absolute top-0 right-0 mt-10 mr-10 p-3 rounded-full font-bold text-white bg-[#ECD71A]/[.12]"
    @click="toggleOnOff"
  >
    <span v-if="isOn">
      <svg
        width="31"
        height="28"
        viewBox="0 0 31 28"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g clip-path="url(#clip0_2124_45999)">
          <path
            d="M0.00585938 13.0703C0.00585938 17.3477 2.93555 20.1836 7.33008 20.1836C11.6543 20.1836 14.5489 17.6406 14.5489 13.8086C14.5489 12.2148 13.9864 10.9258 13.0489 10.1172C12.6153 9.76562 12.3692 9.63672 11.959 9.63672C11.42 9.63672 11.045 9.96484 11.045 10.4453C11.045 11.0312 11.3848 11.1836 11.9239 11.6758C12.4161 12.1562 12.6973 12.8828 12.6973 13.7734C12.6973 16.4922 10.5645 18.3086 7.36524 18.3086C4.08398 18.3086 1.89258 16.2109 1.89258 13.0586C1.89258 11.2539 2.80664 9.55469 4.30664 8.58203L3.36914 6.95312C1.2832 8.25391 0.00585938 10.5859 0.00585938 13.0703ZM3.16992 6.96484C3.16992 9.58984 4.98633 11.4414 7.85742 11.4414C8.36133 11.4414 8.79492 11.0195 8.79492 10.5039C8.79492 9.98828 8.36133 9.55469 7.85742 9.55469C6.12305 9.55469 5.05664 8.46484 5.05664 6.96484C5.05664 5.30078 6.42774 4.14062 8.26758 4.14062C9.12305 4.14062 10.0371 4.39844 10.8809 4.97266L11.9825 3.4375C10.8106 2.61719 9.50977 2.25391 8.2793 2.25391C5.44336 2.25391 3.16992 4.1875 3.16992 6.96484ZM9.41602 6.64844C9.39258 7.25781 9.80274 7.66797 10.3418 7.66797C10.8575 7.66797 11.2559 7.32812 11.2793 6.73047C11.3614 4.50391 12.9786 2.875 15.252 2.875C16.6231 2.875 17.8184 3.60156 18.2989 4.67969C18.3926 4.85547 18.5215 4.86719 18.7442 4.79688C19.1309 4.69141 19.5645 4.63281 19.9864 4.63281C22.084 4.65625 24.0762 6.23828 24.0762 8.75781C24.0762 14.2656 16.3418 13.5039 16.3418 18.8711C16.3418 21.4258 18.3692 23.0312 20.9942 23.0312C21.2754 23.0312 21.5801 23.0078 21.8848 22.9961C22.1543 24.9883 23.4082 26.9219 25.4356 26.9219C28.3653 26.9219 29.795 23.3594 29.795 19.8906C29.795 18.3789 29.7129 17.3594 29.6075 16.3984L27.7207 16.9258C27.8262 17.8633 27.92 18.7422 27.92 19.8672C27.92 22.7148 26.8418 25.0352 25.4356 25.0352C23.9825 25.0352 23.3965 23.1016 23.3965 21.5664C23.3965 21.4375 23.3262 21.3555 23.1621 21.3672C22.834 21.3672 22.3887 21.3789 22.0957 21.3789C19.7637 21.3789 18.2286 20.6523 18.2286 18.8359C18.2286 14.5586 25.9629 15.5195 25.9629 8.75781C25.9629 5.14844 23.2911 2.74609 20.2325 2.74609C19.9981 2.74609 19.67 2.79297 19.3418 2.86328C18.4043 1.70312 16.9043 1 15.2637 1C11.9356 1 9.55664 3.33203 9.41602 6.64844ZM23.1973 18.1445C23.1973 18.6719 23.6192 19.0469 24.1465 19.082C28.1661 19.3398 30.8497 16.9844 30.8497 13.1758C30.8497 10.0586 28.6348 7.67969 25.3067 7.23438L25.0137 9.10938C27.3809 9.14453 28.9629 10.7617 28.9629 13.1758C28.9629 15.8125 27.0293 17.4297 24.1465 17.207C23.6192 17.1602 23.1973 17.6289 23.1973 18.1445ZM17.1739 19.668C16.4825 19.9141 15.6739 20.0312 14.9121 20.0312C12.9317 20.0312 10.9161 19.2578 10.1426 18.0625L8.58398 19.3281C9.81445 20.8633 12.0411 21.918 14.7129 21.918C15.6739 21.918 16.752 21.7773 17.8184 21.4727L17.1739 19.668ZM13.4121 11.3945L14.045 13.1875C16.9981 12.6016 18.3223 10.75 18.3223 8.00781C18.3223 7.49219 17.8887 7.07031 17.3731 7.07031C16.8575 7.07031 16.4356 7.49219 16.4356 8.00781C16.4356 9.94141 15.6153 11.0781 13.4121 11.3945Z"
            fill="#ECD71A"
            fill-opacity="1"
          />
        </g>
        <defs>
          <clipPath id="clip0_2124_45999">
            <rect
              width="30.8438"
              height="25.9336"
              fill="white"
              transform="translate(0.00585938 1)"
            />
          </clipPath>
        </defs>
      </svg>
    </span>
    <span v-else>
      <svg
        width="31"
        height="28"
        viewBox="0 0 31 28"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g clip-path="url(#clip0_2124_46000)">
          <path
            d="M6.54687 20.0312C9.39453 20.0312 11.1406 18.1328 11.1406 15.6719C11.1406 14.8984 10.8125 14.0195 10.3555 13.5742C9.82812 13.0703 9.48828 12.9297 9.48828 12.3438C9.48828 11.8633 9.85156 11.5352 10.4023 11.5352C10.8008 11.5352 11.0586 11.6523 11.4805 12.0156C11.8437 12.332 12.1601 12.7305 12.3828 13.1992C14.1875 12.7773 14.8672 11.6758 14.8672 9.90625C14.8672 9.39062 15.3008 8.95703 15.8164 8.95703C16.332 8.95703 16.7539 9.39062 16.7539 9.90625C16.7656 12.4961 15.5703 14.3008 12.9453 14.9688C12.9687 15.2031 12.9922 15.4492 12.9922 15.707C12.9922 17.8984 12.043 19.668 10.3906 20.7812C11.5625 21.5078 13.0625 21.918 14.5976 21.918C14.8906 21.918 15.2187 21.8945 15.8398 21.8711C15.7109 21.2852 15.6406 20.7344 15.6406 20.207C15.6406 13.2461 25.5078 14.0078 25.5078 7.38672C25.5078 4.63281 22.8359 2.74609 20.2344 2.74609C20 2.74609 19.6719 2.79297 19.3437 2.86328C18.4062 1.70312 16.9062 1 15.5 1C13.0156 1 11.3633 2.61719 11.2812 4.85547C11.2578 5.45312 10.8594 5.79297 10.3437 5.79297C9.80469 5.79297 9.39453 5.38281 9.41797 4.77344C9.45312 3.92969 9.6289 3.15625 9.93359 2.47656C9.38281 2.32422 8.83203 2.25391 8.28125 2.25391C5.44531 2.25391 3.32422 4.04688 3.32422 6.23828C3.32422 7.70312 4.41406 8.91016 5.99609 8.91016C6.51172 8.91016 6.93359 9.34375 6.93359 9.84766C6.93359 10.3633 6.51172 10.7969 5.99609 10.7969C3.94531 10.7969 2.44531 9.84766 1.7539 8.35938C0.652344 9.63672 0.0078125 11.3242 0.0078125 13.0703C0.0078125 17.0898 2.59765 20.0312 6.54687 20.0312ZM25.4375 26.9219C28.3672 26.9219 29.7969 23.3594 29.7969 19.8906C29.7969 19.3633 29.7734 18.8711 29.7617 18.4141C28.7305 18.9414 27.4766 19.1758 26.0351 19.082C25.5078 19.0469 25.0859 18.6719 25.0859 18.1445C25.0859 17.6289 25.5078 17.1602 26.0351 17.207C28.918 17.4297 30.8516 15.8125 30.8516 13.1758C30.8516 10.832 29.5859 8.91016 27.5469 7.9375C26.0586 15.6484 17.6328 14.6172 17.375 19.8672C17.293 21.6367 18.6406 23.0312 20.5625 23.0312C21.2422 23.0312 21.582 23.0078 21.8867 22.9961C22.1562 24.9883 23.4101 26.9219 25.4375 26.9219Z"
            fill="#ECD71A"
          />
        </g>
        <defs>
          <clipPath id="clip0_2124_46000">
            <rect
              width="30.8438"
              height="25.9336"
              fill="white"
              transform="translate(0.0078125 1)"
            />
          </clipPath>
        </defs>
      </svg>
    </span>
  </button>
  <div class="flex justify-center items-center">
    <img src="@/assets/WILWIN.svg" alt="WILWIN Logo" class="mb-44 mt-10 h-11" />
  </div>
  <div class="flex justify-center items-center font-semibold">
    <div class="mr-32 mb-32 text-center text-4xl">
      <button
        class="mb-10 px-4 py-1 uppercase rounded-full text-[#ECD71A] bg-[#ECD71A]/[.12] flex justify-center items-center"
      >
        {{ team1.name }}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="3"
          stroke="currentColor"
          class="ml-3 w-7 h-7"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M19.5 8.25l-7.5 7.5-7.5-7.5"
          />
        </svg>
      </button>
      <p class="score text-7xl font-black text-[#EEEEEE]">{{ team1.score }}</p>
    </div>
    <div class="flex justify-center items-center">
      <button
        class="bg-[#ECD71A] text-[#3B3D33] hover:bg-[#3B3D33] hover:text-[#ECD71A] font-black text-center px-6 py-3 mb-8 rounded-2xl flex flex-col items-center aspect-w-1 aspect-h-1"
      >
        <svg
          class="mb-1.5"
          width="45"
          height="45"
          viewBox="0 0 76 76"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            d="M8.14258 13.211C8.14258 26.3477 14.4406 34.5542 27.0047 38.4028C28.9768 40.8204 31.2034 42.7606 33.3664 44.1283V57.9649H28.3725C23.8876 57.9649 21.5656 60.5413 21.5656 64.7718V70.0202C21.5656 71.4514 22.6789 72.4375 24.0148 72.4375H54.4868C55.8228 72.4375 56.9362 71.4514 56.9362 70.0202V64.7718C56.9362 60.5413 54.5824 57.9649 50.0973 57.9649H45.1353V44.1283C47.2983 42.7606 49.5248 40.8204 51.465 38.4028C64.0612 34.5542 70.3592 26.3477 70.3592 13.211C70.3592 9.93473 68.3234 7.93083 64.92 7.93083H58.7491C58.2401 4.68639 55.9501 2.71429 52.1012 2.71429H26.4004C22.5834 2.71429 20.2614 4.65459 19.7525 7.93083H13.5818C10.1783 7.93083 8.14258 9.93473 8.14258 13.211ZM12.6911 13.6563C12.6911 13.1473 13.0728 12.7338 13.6135 12.7338H19.5935V18.9682C19.5935 23.8348 20.8658 28.3516 22.8379 32.2639C16.19 28.8923 12.6911 22.7215 12.6911 13.6563ZM55.632 32.2639C57.6359 28.3516 58.9081 23.8348 58.9081 18.9682V12.7338H64.888C65.4289 12.7338 65.8106 13.1473 65.8106 13.6563C65.8106 22.7215 62.3116 28.8923 55.632 32.2639Z"
            fill="#3B3D33"
          />
        </svg>
        WHO WILWIN ?
      </button>
    </div>
    <div class="ml-32 mb-32 text-center text-4xl">
      <button
        class="mb-10 px-4 py-1 uppercase rounded-full text-[#ECD71A] bg-[#ECD71A]/[.12] flex justify-center items-center"
      >
        {{ team2.name }}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="3"
          stroke="currentColor"
          class="ml-3 w-7 h-7"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M19.5 8.25l-7.5 7.5-7.5-7.5"
          />
        </svg>
      </button>
      <p class="score text-7xl font-black text-[#EEEEEE]">{{ team2.score }}</p>
    </div>
  </div>
  <div class="flex justify-center text-[#EEEEEE] text-lg font-bold mt-20">
    <div class="text-center mx-16">
      <div class="flex flex-col items-center">
        <label for="input1">Intempéries</label>
        <input
          type="checkbox"
          class="cursor-pointer h-8 w-8 bg-[#ECD71A]/[.12] mt-4 rounded-md checked:bg-yellow-400"
          id="input1"
        />
      </div>
    </div>
    <div class="text-center mx-16">
      <div class="flex flex-col items-center">
        <label for="input2">Température</label>
        <select
          class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center"
          id="input2"
        >
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
        <select
          class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center"
          id="input3"
        >
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
        <select
          class="w-48 h-10 bg-[#ECD71A]/[.12] rounded-full p-1 mt-4 text-center capitalize"
          id="input4"
        >
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
@font-face {
  font-family: "SF Pro Rounded";
  src: url("../assets/SF-Pro-Rounded-Black.otf") format("opentype");
}

.score {
  font-family: "SF Pro Rounded", sans-serif;
}
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
  background-color: #ecd71a;
  color: #3b3d33;
}

button {
  transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out;
}

button:hover svg path {
  fill: #ecd71a;
}

button:hover {
  background-color: #3b3d33;
  color: #ecd71a;
}

input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 30px;
  width: 30px;
  border-radius: 100%;
  background-color: #ecd71a;
  cursor: pointer;
}
</style>

<script>
export default {
  data() {
    return {
      team1: {
        name: "Team 1",
        score: "32%",
      },
      team2: {
        name: "Team 2",
        score: "68%",
      },
      isOn: true,
    };
  },
  methods: {
    toggleOnOff() {
      this.isOn = !this.isOn;
    },
  },
};
</script>
