// store/index.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    isStarted: false,
  },
  mutations: {
    toggleIsStarted(state) {
      state.isStarted = !state.isStarted;
    },
  },
});
