<template>
    <div class="controlbar">
        <div id="timeline-controls" class="top-panel-item">
            <!--     重启按钮-->
            <button id="reset-button" title="Reset the model" class="button-box">
                <img class="material-icons" id="button-top-reset" src="/chehuinew.svg" />
            </button>
            <!--    启动/暂停按钮-->
            <button id="play-pause-button" title="Run/Pause training" @click="togglePlayPause" class="button-box">
                <img class="material-icons button-top-play-pause" id="button-top-play" src="/bofangnew.svg"
                    v-if="!isPlaying" />
                <img class="material-icons button-top-play-pause" id="button-top-pause" src="zantingnew.svg" v-else />
            </button>
            <button id="edit-button" title="edit the config" @click="updateVisiable" class="button-box">
                <img class="material-icons" id="button-top-edit" src="/bianji-2new.svg" />
            </button>
        </div>


        <!--   当前Epoch数量-->
        <div id="iteration" class="top-panel-item">
            <div class="top-column-title">Epoch</div>
            <div id="iteration-count" v-text="iterationCount"></div>
        </div>
    </div>
</template>

<script>

import axios from 'axios';
export default {
    props: {
        iterationCount: {
            default: "0"
        },
    },
    components: {

    },
    data() {
        return {
            // iterationCount: 0,
            isPlaying: false,
            intervalId: null, // 用于存储定时器ID
        };
    },
    computed: {

    },
    methods: {
        togglePlayPause() {
            this.$emit('start-change', !this.isPlaying);
            this.isPlaying = !this.isPlaying;
            // console.log(this.isPlaying)/
            // if (this.isPlaying) {
            //     // 当isPlaying为true，启动定时器自增iterationCount
            //     this.startIncrementing();
            // } else {
            //     // 当isPlaying为false，停止定时器
            //     this.stopIncrementing();
            // }
            // 你的 Express 服务器端的 URL，可能需要进行修改
            let url = 'http://localhost:3000/play_pause';

            // 使用 axios 发送请求
            axios.post(url, {
                isPlaying: this.isPlaying
            })
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.error(error);
                });
        },
        updateVisiable() {
            console.log("updateVisiable")
            this.$emit('updateVisiable');
        },
        // startIncrementing() {
        //     // 每秒自增iterationCount
        //     this.intervalId = setInterval(() => {
        //         const newCount = (parseInt(this.iterationCount) + 1).toString();
        //         this.$emit('update:iterationCount', newCount);
        //     }, 10); // 1000毫秒（1秒）间隔
        // },
        // stopIncrementing() {
        //     // 停止定时器
        //     if (this.intervalId !== null) {
        //         clearInterval(this.intervalId);
        //         this.intervalId = null;
        //     }
        // },
    },
    watch: {
        selected(newVal) {
            console.log('Selected value changed:', newVal)
        },
        iterationCount(newVal) {
            this.$emit('iteration-changed', newVal); // 如果需要，可以发出iterationCount变化的事件
        }
    },
    mounted() {

    },
};
</script>

<style lang="scss" scoped>
.controlbar {
    display: flex;
    justify-content: center;
    /* 水平居中子元素 */
    align-items: center;
    margin-top: 20px;

    #timeline-controls {
        display: flex;
        justify-content: center;
        /* 水平居中子元素 */
        align-items: center;
    }

    .button-box {

        border: none;
        /* 移除边框 */
    }

    #button-top-reset {
        width: 30px;
        height: 30px;
    }

    .button-top-play-pause {
        width: 60px;
        height: 60px;
    }

    #button-top-edit {
        width: 30px;
        height: 30px;
    }

    #iteration {
        font-size: 30px;
    }

    .top-panel-item {
        margin-left: 20px;
        margin-right: 20px;
    }
}
</style>