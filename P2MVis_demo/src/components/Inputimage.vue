<template>
    <div id="distribution-selection" class="top-panel-item">
        <div class="top-column-title">Input Image</div>
        <div id="distribution-image-list">
            <img class="distribution-image" src="input.png" />
            <img class="distribution-image" src="input_2.png" />
            <img class="distribution-image" src="../assets/0.png" />
            <img class="distribution-image" src="../assets/2.png" />
        </div>
        <div id="distribution-selection-checkbox">
            <input type="checkbox" id="toggle-pretrained" v-model="pre_trained" />
            <label for="toggle-pretrained">pre-trained model</label>
        </div>
    </div>
</template>
    
<script>

export default {
    props: {

    },
    components: {

    },
    data() {
        return {
            pre_trained: true,
        };
    },
    computed: {

    },
    methods: {

    },
    watch: {
        selected(newVal) {
            console.log('Selected value changed:', newVal)
        }
    },
    mounted() {

    },
};
</script>
    
<style lang="scss" scoped>
#distribution-selection {
    .top-column-title {
        margin-left: 35px;
    }

    #distribution-image-list {
        height: 30px;
        margin-bottom: 5px;
        display: flex;
        align-items: center;
        margin-left: 35px;

        .distribution-image {
            border: 1px solid #cccccc;
            height: 30px;
            margin-right: 7px;
            width: 30px;
            padding: 0;
            display: block;

        }

    }

    .top-column-title {
        color: #222;
        font-size: 15px;
    }

    #distribution-selection-checkbox {
        display: flex;
        margin-left: 35px;
        /* 水平居中 */
        align-items: center;
        padding: 0;
        margin-bottom: 5px;

        #toggle-pretrained {
            padding: 0;
            line-height: 1;
        }

        label {
            padding: 0;
            line-height: 1;
            margin: 0 0 0 5px;
            font-size: 15px;
        }
    }
}
</style>
    