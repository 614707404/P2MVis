<template>
    <div id="architecture-container" @click="toggleDropdown">
        <div id="seed-control-container" class="hyperparameter">
            <div id="seed-control-text">Initial Model:</div>
            <div id="seed-control-dropdown-container" class="custom-select hyperparameter-dropdown-container">
                <div id="seed-dropdown-box" :style="{ color: dropdownBoxColor, stroke: dropdownBoxStroke }">
                    <div id="seed-dropdown-box-text">{{ seed }}</div>
                    <svg id="seed-dropdown-arrow-svg">
                        <g id="seed-dropdown-arrow-g">
                            <path d="M2 3 l 4.5 5 l 4.5 -5"></path>
                        </g>
                    </svg>
                </div>
                <div id="seed-dropdown-deco" :style="{ opacity: dropdownDecoOpacity }"></div>
                <div id="seed-dropdown-options-container" v-show="seedDropdownExpanded">
                    <div id="seed-dropdown-desc"></div>
                    <p id="seed-dropdown-option-1" class="seed-dropdown-options" @click="seedChanged(1)">Ellipse</p>
                    <p id="seed-dropdown-option-2" class="seed-dropdown-options" @click="seedChanged(2)">Voxel</p>
                    <!-- <p v-for="option in seedOptions" :key="option" :id="`seed-dropdown-option-${option}`"
                        class="seed-dropdown-options" @click="seedChanged(option)">
                        {{ option }}
                    </p> -->
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            seed: 'Ellipse', // 初始化种子值
            seedOptions: [1, 2, 3], // 种子选项
            seedDropdownExpanded: false, // 控制下拉菜单的展开和收起
            compare: false, // 比较状态
            dropdownBoxColor: '#4f900d', // 默认颜色
            dropdownBoxStroke: '#4f900d', // 默认边框颜色
            dropdownDecoOpacity: '0.5', // 默认透明度
            hoveredSeed: null, // 悬停的种子值
            // 其他状态
        };
    },
    methods: {

        toggleDropdown() {
            console.log("toggleDropdown called");
            this.seedDropdownExpanded = !this.seedDropdownExpanded;
        },

        seedChanged(option) {
            if (option == 1) {
                this.seed = "Ellipse";
            } else {
                this.seed = "Voxel";
            }

            // 种子值更改时的逻辑
        },
        // 其他需要的方法
    },
    // 可能会有其他的生命周期钩子或计算属性
};
</script>
  
<style scoped>
/* 这里将会添加组件的样式 */
/* hyperparameter */
#architecture-container {
    /* display: flex;
    justify-content: center;
    align-items: center; */
    display: inline-block;
    position: relative;
    box-sizing: border-box;
    font-size: 18px;
    color: #808080;
    top: 105px;
    width: 100px;
    /* height: 100%;
    width: 100%; */
}

.hyperparameter {
    font-size: 9pt;
    color: #808080;
}

.hyperparameter-dropdown-container {
    display: inline-block;
}

.custom-select {
    background: none;
    /* 移除背景 */
    border: none;
}

.custom-select select {
    font-size: 9pt;
    border-color: #808080;
    border-radius: 3px;
    color: #808080;
}

#seed-control-container {
    display: block;
    opacity: 1;
    /* position: absolute;
    left: 465px;
    top: -60px; */
    color: #4f900d;
    width: auto;
}

#seed-control-text {
    display: inline-block;
    font-size: 18px;
    font-weight: bolder;
    position: absolute;
    top: 2px;
    width: auto;
    white-space: nowrap;
}

#seed-control-dropdown-container {
    width: 100%;
    height: 100%;
    display: inline-block;
    position: relative;
    cursor: pointer;
    right: -37px;
    top: 2px;
}

#seed-dropdown-box {
    position: absolute;
    top: -3px;
    left: 78px;
    width: 80px;
}

#seed-dropdown-box-text {
    display: inline-block;
    width: auto;
    white-space: nowrap;
}

#seed-dropdown-deco {
    width: 50px;
    height: 3px;
    background-color: #4f900d;
    position: absolute;
    z-index: -1;
    left: 79px;
    top: 15px;
    opacity: 0.5;
}

#seed-dropdown-arrow-svg {
    display: inline-block;
    height: 10px;
    width: 13px;
}

#seed-dropdown-arrow-g {
    fill: none;
    stroke: #808080;
    stroke: #4f900d;
}

#seed-dropdown-options-container {

    height: 36px;
    width: 50px;
    box-shadow: 0px 2.5px 5px #00000030;
    position: absolute;
    left: 81px;
    top: 18px;
    text-align: center;
    white-space: nowrap;
}

.seed-dropdown-options {
    padding: 2px 2px;
    background-color: #fafafa;
    cursor: pointer;
    margin: 0;
    border-bottom: 1px solid #f2f2f2;
}

.seed-dropdown-options:hover {
    background-color: #b5e586;
}
</style>
  