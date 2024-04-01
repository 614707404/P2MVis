<template>
    <div class="modeloverview">
        <!-- <div id="cav"> -->
        <!-- <div id="modeloverview-title">MODEL OVERVIEW</div> -->
        <div id="CNN_group">
            <div id="inputimg-title">Input Image</div>
            <div id="inputimg">
                <img src="input.png" style="height: 100%; width: 100%;" :key="this.renderKey" />
            </div>
            <CNNContainer id="CNNcontainer" style="z-index: 11;" v-show="editVisiable"></CNNContainer>
            <div id="CNN_part">
                <!-- <el-popover ref="popover" placement="right" title="标题" width="200" trigger="focus"
                    content="这是一段内容,这是一段内容,这是一段内容,这是一段内容。">
                </el-popover> -->
                <!-- <div id="CNN_title" v-popover:popover>Image Feature Network</div> -->
                <div id="CNN_title">Image Feature Network</div>

                <!-- <div id="CNN_explain">extract perceptual feature from the input image</div> -->
                <div id="feature1" class="feature" @click="featureClick_1"></div>
                <div id="feature2" class="feature" @click="featureClick_2"></div>
                <div id="feature3" class="feature" @click="featureClick_3"></div>
                <!-- <div id="legend"></div> -->
                <div id="CNN_func" v-show="editVisiable">extract perceptual feature</div>
                <!-- <div id="CNN-layer-1" class="CNN-layers">conv3_3</div>
                <div id="CNN-layer-2" class="CNN-layers">conv4_3</div>
                <div id="CNN-layer-3" class="CNN-layers">conv5_3</div> -->
            </div>


            <svg class="overlay-svg" viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <!-- 用作箭头的 marker -->
                    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3"
                        stroke="#7097c8" orient="auto-start-reverse">
                        <path d="M 0 0 L 10 5 L 0 10 z" fill="#7097c8" />
                    </marker>
                    <marker id="arrowGray" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3"
                        orient="auto-start-reverse">
                        <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(128, 128, 128, 0.5)" />
                    </marker>
                </defs>

                <!-- 带标记的线 -->
                <!-- stroke-dasharray="1,1" 虚线-->
                <line x1="44" y1="41" x2="79" y2="41" stroke="#7097c8"
                    :marker-end="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow)' : 'url(#arrowGray)'"
                    :class="[{ 'flowing-dash-1': isStarted }, 'grayed-out-1']" />
                <line x1="121" y1="41" x2="134" y2="41" stroke="#7097c8"
                    :marker-end="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow)' : 'url(#arrowGray)'"
                    :class="[{ 'flowing-dash-1': isStarted }, 'grayed-out-1']" />
                <line x1="176" y1="41" x2="189" y2="41" stroke="#7097c8"
                    :marker-end="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow)' : 'url(#arrowGray)'"
                    :class="[{ 'flowing-dash-1': isStarted }, 'grayed-out-1']" />
                <!-- <path
                    d="M 100 65
                    C 110 75, 120 75, 130 65
                    C 140 55, 150 55, 160 65"
                    stroke="black"
                    fill="none"
                    transform="rotate(45, 100, 65)"
                    marker-end="url(#arrow)" /> -->
                <path d="M 100 65
                        C 100 71, 108 77, 127 77
                        C 146 77, 155 82, 155 98" stroke="#7097c8" fill="none"
                    :marker-end="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow)' : 'url(#arrowGray)'"
                    :class="[{ 'flowing-dash-1': isStarted }, 'grayed-out-1']" />
                <path d="M 210 65
                        C 210 71, 202 77, 183 77
                        C 164 77, 155 82, 155 98" stroke="#7097c8" fill="none"
                    :marker-end="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow)' : 'url(#arrowGray)'"
                    :class="[{ 'flowing-dash-1': isStarted }, 'grayed-out-1']" />
                <line x1="155" y1="65" x2="155" y2="98" stroke="#7097c8"
                    :marker-end="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow)' : 'url(#arrowGray)'"
                    :class="[{ 'flowing-dash-1': isStarted }, 'grayed-out-1']" />


                <path d="M 60 35
                        C 60 27, 48 21, 74 22" stroke="gray" fill="none" marker-start="url(#arrow-small)"
                    stroke-width="0.7" stroke-dasharray="3,1" v-show="editVisiable" />
                <!-- 带标记的曲线-->
                <!-- <path
                    d="M 110 10
                    C 120 20, 130 20, 140 10
                    C 150 0, 160 0, 170 10
                    C 180 20, 190 20, 200 10"
                    stroke="blue"
                    fill="none"
                    marker-start="url(#arrow)"
                    marker-mid="url(#arrow)"
                    marker-end="url(#arrow)" /> -->
            </svg>
        </div>

        <div id="PerceptualFeaturePooling">
            <div id="pooling">
                <div id="pooling_title">Perceptual Feature Pooling</div>
            </div>
            <svg id="shadow" width="480" height="500" xmlns="http://www.w3.org/2000/svg">
                <!-- <path d="M 100,300 
                        A 280,200 0 0 1 480,500 
                        L 480,0 
                        A 280,200 0 0 1 100,200 
                        L 100,280" fill="#fbf2e2" /> -->
            </svg>
        </div>







        <!-- <span class="annotation annotation1">Input Image</span>
        <span class="annotation annotation2">Ellipsoid Mesh</span>
        <span class="annotation annotation3">156 vertices</span>
        <span class="annotation annotation4">628 vertices</span>
        <span class="annotation annotation5">2466 vertices</span>
        <span class="annotation annotation6">Perceptual Feature Pooling</span>
        <span class="annotation annotation7">224x224x3</span>
        <span class="annotation annotation8">112x112x32</span>
        <span class="annotation annotation9">28x28x128</span> -->

        <div id="GCN_group">
            <div id="initmodel">
                <img src="orig.png" style="height: 100%; width: 100%;" />
            </div>
            <div id="InitialModel">Initial Model</div>
            <!-- <InitModel id="InitModel" v-show="editVisiable"></InitModel> -->
            <div id="GCN_part">
                <div id="GCN_title">Mesh Deformation Blocks</div>
                <div id="unpooling-tag-1" class="unpooling-tags" v-show="editVisiable">Unpooling</div>
                <div id="unpooling-tag-2" class="unpooling-tags" v-show="editVisiable">Unpooling</div>
                <div id="vertices-tag-1" class="vertices-tags">156 vertices</div>
                <div id="vertices-tag-2" class="vertices-tags">628 vertices</div>
                <div id="vertices-tag-3" class="vertices-tags">2466 vertices</div>
                <div id="model1" class="model" @click="modelClick_1">
                    <ThreeModel :objPath="'predict1.obj'" :key="this.renderKey"></ThreeModel>
                </div>
                <div id="model2" class="model" @click="modelClick_2">
                    <ThreeModel :objPath="'predict2.obj'" :key="this.renderKey"></ThreeModel>
                </div>
                <div id="model3" class="model" @click="modelClick_3">
                    <ThreeModel :objPath="'predict3.obj'" :key="this.renderKey"></ThreeModel>
                </div>
                <div id="loss" v-show="editVisiable">
                    <LossContainer id="losscontainer"></LossContainer>
                    <CharmerContainer id="charmercontainer"></CharmerContainer>
                    <NormalContainer id="normalcontainer"></NormalContainer>
                </div>
                <div id="opti-learning" v-show="editVisiable">
                    <Optimizer id="optimizer"></Optimizer>
                    <LearningRate id="learningrate"></LearningRate>
                </div>

            </div>
            <svg class="overlay-svg-2" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <!-- 用作箭头的 marker -->
                    <marker id="arrow1" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3"
                        stroke="#4f900d" orient="auto-start-reverse">
                        <path d="M 0 0 L 10 5 L 0 10 z" fill="#4f900d" />
                    </marker>
                    <marker id="arrowGray1" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3" markerHeight="3"
                        orient="auto-start-reverse">
                        <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(128, 128, 128, 0.5)" />
                    </marker>
                </defs>

                <!-- 带标记的线 -->
                <!-- stroke-dasharray="1,1" 虚线-->
                <line x1="44" y1="56" x2="85" y2="56" stroke="#4f900d"
                    :marker-end="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow1)' : 'url(#arrowGray1)'"
                    class="grayed-out-2" />
                <line x1="140" y1="56" x2="127.5" y2="56" stroke="#4f900d"
                    :marker-start="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow1)' : 'url(#arrowGray1)'"
                    :class="[{ 'flowing-dash': isStarted }, 'grayed-out-2']" />
                <line x1="195" y1="56" x2="182" y2="56" stroke="#4f900d"
                    :marker-start="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow1)' : 'url(#arrowGray1)'"
                    :class="[{ 'flowing-dash': isStarted }, 'grayed-out-2']" />
                <!-- <path
                    d="M 100 65
                    C 110 75, 120 75, 130 65
                    C 140 55, 150 55, 160 65"
                    stroke="black"
                    fill="none"
                    transform="rotate(45, 100, 65)"
                    marker-end="url(#arrow)" /> -->
                <path d="M 100 33
                        C 100 27, 108 21, 127 21
                        C 146 21, 155 16, 155 0" stroke="#4f900d" fill="none"
                    :marker-start="isClicked1 ? 'url(#arrow1)' : 'url(#arrowGray1)'"
                    :class="[{ 'flowing-dash': isStarted }, 'grayed-out-11']" />
                <path d="M 210 33
                        C 210 27, 202 21, 183 21
                        C 164 21, 155 16, 155 0" stroke="#4f900d" fill="none"
                    :marker-start="isClicked2 ? 'url(#arrow1)' : 'url(#arrowGray1)'"
                    :class="[{ 'flowing-dash': isStarted }, 'grayed-out-22']" />

                <line x2="155" y2="0" x1="155" y1="33" stroke="#4f900d"
                    :marker-start="isClicked3 ? 'url(#arrow1)' : 'url(#arrowGray1)'"
                    :class="[{ 'flowing-dash': isStarted }, 'grayed-out-33']" />

                <path d=" M 105,76.6 C 105,95 110,100 115,100 L 237,100 C 242,100 247,95 247,90 L 247,65 C 247,60
                    242,55 237,55 L 237,55 " stroke=" #4f900d" fill="transparent" stroke-width="1"
                    :marker-start="(isClicked1 || isClicked2 || isClicked3) ? 'url(#arrow1)' : 'url(#arrowGray1)'"
                    :class="[{ 'flowing-dash': isStarted }, 'grayed-out-2']" />

                <!-- 带标记的曲线-->
                <!-- <path
                    d="M 110 10
                    C 120 20, 130 20, 140 10
                    C 150 0, 160 0, 170 10
                    C 180 20, 190 20, 200 10"
                    stroke="blue"
                    fill="none"
                    marker-start="url(#arrow)"
                    marker-mid="url(#arrow)"
                    marker-end="url(#arrow)" /> -->
            </svg>
        </div>






        <!-- <div id="gradient"></div> -->

        <!-- <svg ref="svg" style="height: 100%; width: 100%;"></svg> -->
        <!-- <div id="CNN-config" class="config-item" v-show="editVisiable">
            <label>CNN:</label>
            <b-form-select v-model="CNN" :options="CNN_options" id="CNN-select"></b-form-select>
        </div>
        <div id="hidden-config" class="config-item" v-show="editVisiable">
            <div id="Hidden-spin">
                <b-form-spinbutton v-model="value" min="0" max="10"></b-form-spinbutton>
            </div>
            <label>hidden layer(s)</label>
        </div>
        <div id="lossing-config" class="config-item" v-show="editVisiable">
            <label>Loss = </label>
            <b-form-spinbutton v-model="value_" min="0" max="10" class="spin-item"></b-form-spinbutton>
            <label>Chamfer loss + </label>
            <b-form-spinbutton v-model="value_" min="0" max="10" class="spin-item"></b-form-spinbutton>
            <label>Normal loss + </label>
            <b-form-spinbutton v-model="value_" min="0" max="10" class="spin-item"></b-form-spinbutton>
            <label>Regularization</label>
        </div>
        <div id="Init-config" class="config-item" v-show="editVisiable">
            <label>Initial Model:</label>
            <b-form-select v-model="Model" :options="Model_options" id="Model-select"></b-form-select>
        </div>
        <div id="unpooling-config" class="config-item" v-show="editVisiable">
            <label>unpooling:</label>
            <b-form-select v-model="unpooling" :options="unpooling_options" id="unpooling-item"></b-form-select>
        </div>
        <div id="l_rate-config" class="config-item" v-show="editVisiable">
            <label>Learing rate:</label>
            <b-form-select v-model="l_rate" :options="l_rate_options" id="l_rate-item"></b-form-select>
        </div>
        <div id="optimizer-config" class="config-item" v-show="editVisiable">
            <label>Optimizer:</label>
            <b-form-select v-model="optimizer" :options="optimizer_options" id="optimizer-item"></b-form-select>
        </div> -->
        <!-- </div> -->
    </div>
</template>

<script>
import * as d3 from 'd3'
// import { BFormSelect } from 'bootstrap-vue'
// import { BFormSpinbutton } from 'bootstrap-vue'
import ThreeModel from './ThreeModel.vue';
import CNNContainer from './CNNContainer.vue';
import InitModel from './InitModel.vue'
import LossContainer from './LossContainer.vue';
import CharmerContainer from './CharmerContainer.vue'
import NormalContainer from './NormalContainer.vue'
import Optimizer from './Optimizer.vue'
import LearningRate from './LearningRate.vue'

export default {
    props: {
        editVisiable: false,
        img_feat_data: {},
        isStarted: true,
    },
    components: {
        // BFormSelect,
        // BFormSpinbutton,
        ThreeModel,
        CNNContainer,
        InitModel,
        LossContainer,
        CharmerContainer,
        NormalContainer,
        Optimizer,
        LearningRate
    },
    data() {
        return {
            // isStarted: true,
            isClicked1: false,
            isClicked2: false,
            isClicked3: false,
            renderKey: 0,
            value: 5,
            value_: 1,
            CNN: 'VGG',
            CNN_options: [
                { value: 'VGG', text: 'VGG' },
                { value: 'ResNet', text: 'ResNet' },
            ],
            Model: 'Ellipse',
            Model_options: [
                { value: 'Ellipse', text: 'Ellipse' },
                { value: 'Voxel', text: 'Voxel' },
            ],
            unpooling: 'Edge',
            unpooling_options: [
                { value: 'Edge', text: 'Edge' },
                { value: 'Face', text: 'Face' },
            ],
            l_rate: '0.001',
            l_rate_options: [
                { value: '0.001', text: '0.001' },
                { value: '0.003', text: '0.003' },
                { value: '0.1', text: '0.1' },
                { value: '0.3', text: '0.3' },
            ],
            optimizer: 'Adam',
            optimizer_options: [
                { value: 'Adam', text: 'Adam' },
                { value: 'SGD', text: 'SGD' },
            ],

            // imgPath: 'input.png',
            paths: [],
            feature_1_flag: true,
            feature_2_flag: true,
            feature_3_flag: true,
            model_1_flag: true,
            model_2_flag: true,
            model_3_flag: true,
        };
    },
    computed: {

    },
    methods: {
        // test() {
        //     console.log("toggleDropdown called");
        // },
        // imgPathWithCounter() {
        //     // 通过添加查询参数来更改图片的URL，这样浏览器就会重新加载图片
        //     return this.imgPath;
        // },
        featureClick_1() {
            this.$emit('change_path', { str1: 'feature', str2: 'C5.8.zip' });
            if (this.feature_1_flag) {
                for (let i = 0; i < this.paths.length; i++) {
                    if (i == 0 || i == 4 || i == 3 || i == 5 || i == 6 || i == 9 || i == 12 || i == 15 || i == 16) {
                        this.paths[i]
                            .attr('stroke', 'blue')  // 改变颜色
                            .attr('stroke-width', 5);
                    } else {
                        this.paths[i]
                            .attr('stroke', 'black')
                            .attr('stroke-width', 1);
                    }
                }

                this.feature_1_flag = false
            } else {
                for (let i = 0; i < this.paths.length; i++) {

                    this.paths[i]
                        .attr('stroke', 'black')
                        .attr('stroke-width', 1);

                }
                this.model_1_flag = true
                this.model_2_flag = true
                this.model_3_flag = true
                this.feature_1_flag = true
                this.feature_2_flag = true
                this.feature_3_flag = true
            }

        },
        featureClick_2() {
            this.$emit('change_path', { str1: 'feature', str2: 'C1.8.zip' });
            if (this.feature_2_flag) {
                for (let i = 0; i < this.paths.length; i++) {
                    if (i == 0 || i == 4 || i == 1 || i == 3 || i == 5 || i == 7 || i == 10 || i == 13 || i == 15 || i == 16) {
                        this.paths[i]
                            .attr('stroke', 'blue')  // 改变颜色
                            .attr('stroke-width', 5);
                    } else {
                        this.paths[i]
                            .attr('stroke', 'black')
                            .attr('stroke-width', 1);
                    }
                }

                this.feature_2_flag = false
            } else {
                for (let i = 0; i < this.paths.length; i++) {

                    this.paths[i]
                        .attr('stroke', 'black')
                        .attr('stroke-width', 1);

                }
                this.model_1_flag = true
                this.model_2_flag = true
                this.model_3_flag = true
                this.feature_1_flag = true
                this.feature_2_flag = true
                this.feature_3_flag = true
            }

        },
        featureClick_3() {
            this.$emit('change_path', { str1: 'feature', str2: 'C2.8.zip' });
            if (this.feature_3_flag) {
                for (let i = 0; i < this.paths.length; i++) {
                    if (i == 0 || i == 4 || i == 1 || i == 2 || i == 3 || i == 5 || i == 8 || i == 11 || i == 14 || i == 15 || i == 16) {
                        this.paths[i]
                            .attr('stroke', 'blue')  // 改变颜色
                            .attr('stroke-width', 5);
                    } else {
                        this.paths[i]
                            .attr('stroke', 'black')
                            .attr('stroke-width', 1);
                    }
                }

                this.feature_3_flag = false
            } else {
                for (let i = 0; i < this.paths.length; i++) {

                    this.paths[i]
                        .attr('stroke', 'black')
                        .attr('stroke-width', 1);

                }
                this.model_1_flag = true
                this.model_2_flag = true
                this.model_3_flag = true
                this.feature_1_flag = true
                this.feature_2_flag = true
                this.feature_3_flag = true
            }

        },
        modelClick_1() {
            // this.isStarted = !this.isStarted;
            if (!this.isClicked1) {
                this.isClicked1 = !this.isClicked1
                const lines = document.querySelectorAll('.grayed-out-11');
                lines.forEach(line => {
                    line.classList.remove('grayed-out-11');
                    line.classList.add('active-11');
                });
                const lines1 = document.querySelectorAll('.grayed-out-1');
                lines1.forEach(line => {
                    line.classList.remove('grayed-out-1');
                    line.classList.add('active-1');
                });
                const lines2 = document.querySelectorAll('.grayed-out-2');
                lines2.forEach(line => {
                    line.classList.remove('grayed-out-2');
                    line.classList.add('active-2');
                });
            } else {
                this.isClicked1 = !this.isClicked1
                const lines = document.querySelectorAll('.active-11');
                lines.forEach(line => {
                    line.classList.remove('active-11');
                    line.classList.add('grayed-out-11');
                });
                const lines1 = document.querySelectorAll('.active-1');
                lines1.forEach(line => {
                    line.classList.remove('active-1');
                    line.classList.add('grayed-out-1');
                });
                const lines2 = document.querySelectorAll('.active-2');
                lines2.forEach(line => {
                    line.classList.remove('active-2');
                    line.classList.add('grayed-out-2');
                });
            }

            this.$emit('change_path', { str1: 'model', str2: 'predict1.obj' });
            if (this.model_1_flag) {
                for (let i = 0; i < this.paths.length; i++) {
                    if (i == 0 || i == 1 || i == 2 || i == 3 || i == 4 || i == 5 || i == 6 || i == 7 || i == 8 || i == 15 || i == 16) {
                        this.paths[i]
                            .attr('stroke', 'blue')  // 改变颜色
                            .attr('stroke-width', 5);
                    } else {
                        this.paths[i]
                            .attr('stroke', 'black')
                            .attr('stroke-width', 1);
                    }
                }

                this.model_1_flag = false
            } else {
                for (let i = 0; i < this.paths.length; i++) {

                    this.paths[i]
                        .attr('stroke', 'black')
                        .attr('stroke-width', 1);

                }
                this.feature_1_flag = true
                this.feature_2_flag = true
                this.feature_3_flag = true
                this.model_1_flag = true
                this.model_2_flag = true
                this.model_3_flag = true
            }

        },
        modelClick_2() {
            if (!this.isClicked3) {
                this.isClicked3 = !this.isClicked3
                const lines = document.querySelectorAll('.grayed-out-33');
                lines.forEach(line => {
                    line.classList.remove('grayed-out-33');
                    line.classList.add('active-33');
                });
                const lines1 = document.querySelectorAll('.grayed-out-1');
                lines1.forEach(line => {
                    line.classList.remove('grayed-out-1');
                    line.classList.add('active-1');
                });
                const lines2 = document.querySelectorAll('.grayed-out-2');
                lines2.forEach(line => {
                    line.classList.remove('grayed-out-2');
                    line.classList.add('active-2');
                });
            } else {
                this.isClicked3 = !this.isClicked3
                const lines = document.querySelectorAll('.active-33');
                lines.forEach(line => {
                    line.classList.remove('active-33');
                    line.classList.add('grayed-out-33');
                });
                const lines1 = document.querySelectorAll('.active-1');
                lines1.forEach(line => {
                    line.classList.remove('active-1');
                    line.classList.add('grayed-out-1');
                });
                const lines2 = document.querySelectorAll('.active-2');
                lines2.forEach(line => {
                    line.classList.remove('active-2');
                    line.classList.add('grayed-out-2');
                });
            }
            this.$emit('change_path', { str1: 'model', str2: 'predict2.obj' });

            if (this.model_2_flag) {
                for (let i = 0; i < this.paths.length; i++) {
                    if (i == 0 || i == 1 || i == 2 || i == 3 || i == 4 || i == 5 || i == 9 || i == 10 || i == 11 || i == 15 || i == 16) {
                        this.paths[i]
                            .attr('stroke', 'blue')  // 改变颜色
                            .attr('stroke-width', 5);
                    } else {
                        this.paths[i]
                            .attr('stroke', 'black')
                            .attr('stroke-width', 1);
                    }
                }

                this.model_2_flag = false
            } else {
                for (let i = 0; i < this.paths.length; i++) {

                    this.paths[i]
                        .attr('stroke', 'black')
                        .attr('stroke-width', 1);

                }
                this.feature_1_flag = true
                this.feature_2_flag = true
                this.feature_3_flag = true
                this.model_1_flag = true
                this.model_2_flag = true
                this.model_3_flag = true
            }

        },
        modelClick_3() {
            if (!this.isClicked2) {
                this.isClicked2 = !this.isClicked2
                const lines = document.querySelectorAll('.grayed-out-22');
                lines.forEach(line => {
                    line.classList.remove('grayed-out-22');
                    line.classList.add('active-22');
                });
                const lines1 = document.querySelectorAll('.grayed-out-1');
                lines1.forEach(line => {
                    line.classList.remove('grayed-out-1');
                    line.classList.add('active-1');
                });
                const lines2 = document.querySelectorAll('.grayed-out-2');
                lines2.forEach(line => {
                    line.classList.remove('grayed-out-2');
                    line.classList.add('active-2');
                });
            } else {
                this.isClicked2 = !this.isClicked2
                const lines = document.querySelectorAll('.active-22');
                lines.forEach(line => {
                    line.classList.remove('active-22');
                    line.classList.add('grayed-out-22');
                });
                const lines1 = document.querySelectorAll('.active-1');
                lines1.forEach(line => {
                    line.classList.remove('active-1');
                    line.classList.add('grayed-out-1');
                });
                const lines2 = document.querySelectorAll('.active-2');
                lines2.forEach(line => {
                    line.classList.remove('active-2');
                    line.classList.add('grayed-out-2');
                });
            }
            this.$emit('change_path', { str1: 'model', str2: 'predict3.obj' });

            if (this.model_3_flag) {
                for (let i = 0; i < this.paths.length; i++) {
                    if (i == 0 || i == 1 || i == 2 || i == 3 || i == 4 || i == 5 || i == 12 || i == 13 || i == 14 || i == 15 || i == 16) {
                        this.paths[i]
                            .attr('stroke', 'blue')  // 改变颜色
                            .attr('stroke-width', 5);
                    } else {
                        this.paths[i]
                            .attr('stroke', 'black')
                            .attr('stroke-width', 1);
                    }
                }

                this.model_3_flag = false
            } else {
                for (let i = 0; i < this.paths.length; i++) {

                    this.paths[i]
                        .attr('stroke', 'black')
                        .attr('stroke-width', 1);

                }
                this.feature_1_flag = true
                this.feature_2_flag = true
                this.feature_3_flag = true
                this.model_1_flag = true
                this.model_2_flag = true
                this.model_3_flag = true
            }

        },
        drawHeatmap(data, elementId) {
            d3.select(elementId).selectAll("svg").remove();
            const parentElement = d3.select(elementId).node();
            const width = parentElement.clientWidth;
            const height = parentElement.clientHeight;

            const svg = d3.select(elementId)
                .append("svg")
                .attr("width", width)
                .attr("height", height)

            const colorScale = d3.scaleSequential(d3.interpolateBlues)
                .domain([d3.min(data, d => d3.min(d)), d3.max(data, d => d3.max(d))]);

            const rows = data.length;
            const cols = data[0].length;

            data.forEach((row, i) => {
                row.forEach((value, j) => {
                    svg.append("rect")
                        .attr("x", j * width / cols)
                        .attr("y", i * height / rows)
                        .attr("width", width / cols)
                        .attr("height", height / rows)
                        .attr("fill", colorScale(value))
                        .on("mouseover", function () {
                            d3.select(this)
                                .attr("stroke", "black")
                                .attr("stroke-width", 2);
                        })
                        .on("mouseout", function () {
                            d3.select(this)
                                .attr("stroke", null);
                        });
                });
            });
            const legendWidth = 100;
            const legendHeight = 20;
            const legendMargin = { top: 10, right: 20, bottom: 10, left: 20 };
            let text = "conv3_3"; // 替换为你想显示的文本
            if (elementId === "#feature2") {
                text = "conv4_3"
            } else if (elementId === "#feature3") {
                text = "conv5_3"
            }



            const textStyle = "font-size: 18px;font-weight: bolder;font-style: italic;color: #004949;"; // 设置文本样式
            const textX = 10; // X轴位置（左边距）
            const textY = height - 20; // Y轴位置（底部边距）

            svg.append("text")
                .attr("x", textX)
                .attr("y", textY)
                .style("text-anchor", "start") // 文本对齐方式
                .attr("dy", "0.35em") // 垂直对齐
                .style("font-family", "sans-serif") // 字体
                .style("font-size", "35px")
                .style("font-weight", "bolder")
                .style("font-style", "italic")
                .style("color", "#004949")
                .text(text);
        },
        drawLegend(svg, colorScale) {
            // 定义标尺的尺寸
            const legendHeight = 200;
            const legendWidth = 20;

            // 创建线性渐变
            const linearGradient = svg.append("defs")
                .append("linearGradient")
                .attr("id", "vertical-gradient")
                .attr("x1", "0%")
                .attr("y1", "100%")
                .attr("x2", "0%")
                .attr("y2", "0%"); // 垂直渐变

            linearGradient.selectAll("stop")
                .data(colorScale.ticks().map((t, i, n) => ({ offset: `${100 * i / n.length}%`, color: colorScale(t) })))
                .enter().append("stop")
                .attr("offset", d => d.offset)
                .attr("stop-color", d => d.color);

            // 添加渐变矩形作为标尺
            svg.append("rect")
                .attr("x", 0)
                .attr("y", 0)
                .attr("width", legendWidth)
                .attr("height", legendHeight)
                .style("fill", "url(#vertical-gradient)");

            // 添加标尺刻度
            // const legendScale = d3.scaleLinear()
            // .domain(colorScale.domain())
            // .range([legendHeight, 0]);

            // const legendAxis = d3.axisRight(legendScale)
            // .ticks(5); // 调整刻度数量

            // svg.append("g")
            // .attr("class", "legend axis")
            // .attr("transform", `translate(${legendWidth}, 0)`)
            // .call(legendAxis);
        }
    },
    watch: {
        editVisiable(newVal, oldVal) {
            console.log('editVisiable changed from', oldVal, 'to', newVal);
        },
        isStarted(newVal, oldVal) {
            console.log('isStarted changed from', oldVal, 'to', newVal);
        },
        img_feat_data(img_feat_data) {
            // 创建颜色比例尺
            // const colorScale = d3.scaleLinear()
            //      .domain([0, 100]) // 假设数据范围是0到100
            //      .range(["#276419", "#ffffff"]); // 从深绿到白色

            const colorScale = d3.scaleSequential(d3.interpolateBlues)
                .domain([0, 100]); // 假设数据范围是0到100

            // 创建SVG容器
            const svg = d3.select("#legend")
                .append("svg")
                .attr("width", 60) // 宽度足以容纳标尺和刻度
                .attr("height", 200); // 高度根据需求设定

            // 调用drawLegend函数
            this.drawLegend(svg, colorScale);

            const parsedData = JSON.parse(img_feat_data);
            console.log("parsedData", parsedData);
            ++this.renderKey;
            this.drawHeatmap(parsedData.x1[0], "#feature1");
            this.drawHeatmap(parsedData.x2[0], "#feature2");
            this.drawHeatmap(parsedData.x3[0], "#feature3");
        }
    },
    mounted() {
        const svg = d3.select(this.$refs.svg)

        const lineGenerator = d3.line().curve(d3.curveBasis)
        const allPoints = [
            [
                [200, 150],
                [350, 150]
            ], [
                [550, 150],
                [650, 150]
            ], [
                [850, 150],
                [950, 150]
            ], [
                [200, 500],
                [350, 500]
            ], [
                [550, 500],
                [650, 500]
            ], [
                [850, 500],
                [950, 500]
            ], [
                [450, 250],
                [450, 400]
            ], [
                [750, 250],
                [750, 325],
                [450, 325],
                [450, 400]
            ], [
                [1050, 250],
                [1050, 325],
                [450, 325],
                [450, 400]
            ], [
                [450, 250],
                [450, 325],
                [750, 325],
                [750, 400]
            ], [
                [750, 250],
                [750, 400]
            ], [
                [1050, 250],
                [1050, 325],
                [750, 325],
                [750, 400]
            ], [
                [450, 250],
                [450, 325],
                [1050, 325],
                [1050, 400]
            ], [
                [750, 250],
                [750, 325],
                [1050, 325],
                [1050, 400]
            ], [
                [1050, 250],
                [1050, 400]
            ], [
                [1050, 600],
                [1050, 700],
                [700, 700]
            ], [
                [700, 700],
                [450, 700],
                [450, 600]
            ]
        ]
        // 
        // for (let points of allPoints) {
        //     const path = svg.append('path')
        //                     .attr('d', lineGenerator(points))
        //                     .attr('stroke', 'black')
        //                     .attr('fill', 'none')
        //                     .attr('stroke-dasharray','5,5')
        //     this.paths.push(path);
        //     const totalLength = path.node().getTotalLength()
        //     function animateLine() {
        //         path.attr('stroke-dashoffset', totalLength)
        //             .transition()
        //             .duration(totalLength * 100)  // 动画的持续时间，单位是毫秒
        //             .ease(d3.easeLinear)  // 动画的缓动函数
        //             .attr('stroke-dashoffset', -totalLength)
        //             .on('end', animateLine)
        //     }

        //     animateLine()
        // }

    },
};
</script>

<style lang="scss" scoped>
.modeloverview {
    background-color: #eee;
    // border-bottom: 2px solid #ddd;
    width: 1200px;
    height: 1000px;
    position: relative;

    #modeloverview-title {
        position: absolute;
        left: -100px;
        font-size: 50px;

    }

    // overflow: hidden; /* 如果组件超出容器，则隐藏其余部分 */
    // position: relative;
    // #cav{
    //     width: 100%;
    //     height: 100%;
    //     transform-origin: top left; /* 设置缩放的基点 */
    //     transform: scale(0.7); /* 设置缩放比例，例如 0.5 会将其缩小到50% */
    //     position: absolute; /* 使其脱离正常文档流 */
    //     top: 0;
    //     left: 0;
    .annotation {
        position: absolute;
        padding: 5px;
        /* You'll need to adjust the top and left values based on your specific needs */
    }

    /* Example annotation positions */
    .annotation1 {
        top: 70px;
        left: 95px;
    }

    .annotation2 {
        top: 420px;
        left: 95px;
    }

    .annotation3 {
        top: 595px;
        left: 345px;
    }

    .annotation4 {
        top: 595px;
        left: 645px;
    }

    .annotation5 {
        top: 595px;
        left: 945px;
    }

    .annotation6 {
        top: 310px;
        left: 345px;
    }

    .annotation7 {
        top: 25px;
        left: 345px;
    }

    .annotation8 {
        top: 25px;
        left: 645px;
    }

    .annotation9 {
        top: 25px;
        left: 945px;
    }

    /* Add more as needed */
    #gradient {
        width: 100px;
        height: 100px;
        background-color: bisque;
        position: absolute;
        top: 650px;
        left: 700px;
    }

    /* 初始样式 */
    .grayed-out-1 {
        stroke: rgba(128, 128, 128, 0.1);
        /* 淡灰色，带有透明度 */
    }

    .grayed-out-2 {
        stroke: rgba(128, 128, 128, 0.1);
        /* 淡灰色，带有透明度 */
    }

    .grayed-out-11 {
        stroke: rgba(128, 128, 128, 0.1);
        /* 淡灰色，带有透明度 */
    }

    .grayed-out-22 {
        stroke: rgba(128, 128, 128, 0.1);
        /* 淡灰色，带有透明度 */
    }

    .grayed-out-33 {
        stroke: rgba(128, 128, 128, 0.1);
        /* 淡灰色，带有透明度 */
    }

    /* 激活时的样式 */
    .active-1 {
        stroke: #7097c8;
        /* 绿色 */
    }

    .active-2 {
        stroke: #4f900d;
        /* 绿色 */
    }

    .active-11 {
        stroke: #4f900d;
        /* 绿色 */
    }

    .active-22 {
        stroke: #4f900d;
        /* 绿色 */
    }

    .active-33 {
        stroke: #4f900d;
        /* 绿色 */
    }

    #CNN_group {
        position: relative;
        width: 1500px;
        height: 400px;

        #CNNcontainer {
            position: absolute;
            top: 175px;
            left: 245px;
        }

        .overlay-svg {
            position: absolute;
            top: 0;
            left: 0;
            z-index: 10;
            /* 较高的z-index确保SVG在顶部 */
        }

        // .CNN-layers {
        //     font-size: 18px;
        //     font-weight: bolder;
        //     font-style: italic;
        //     color: #004949;
        //     z-index: 10;
        // }

        #inputimg-title {
            position: absolute;
            top: 70px;
            left: 70px;
            // color: #205596;
            /* 文字颜色为蓝色 */
            font-family: Arial;
            /* 字体为Arial */
            text-align: center;
            /* 文本居中对齐 */

            font-size: 35px;
            font-weight: bolder;
        }

        #inputimg {
            width: 150px;
            height: 150px;
            border-color: #7097c8;
            border-width: 3px;
            border-style: solid;
            border-radius: 5px;
            position: absolute;
            top: 127px;
            left: 70px;
        }

        #CNN_part {
            position: absolute;
            top: 50px;
            background-color: #edf5ff;
            border-width: 3px;
            border-style: solid;
            border-color: #7097c8;
            border-radius: 5px;
            width: 925px;
            height: 300px;
            left: 350px;

            .feature {
                width: 200px;
                height: 200px;
                background-color: aqua;
                position: absolute;
                top: 70px;

            }

            #feature1 {
                left: 50px;
                z-index: 50;
            }

            #feature2 {
                left: 325px;
                z-index: 50;
            }

            #feature3 {
                left: 600px;
                z-index: 50;
            }

            #legend {
                position: absolute;
                top: 70px;
                left: 850px;
            }

            #CNN_title {
                // color: #205596;
                /* 文字颜色为蓝色 */
                font-family: Arial;
                /* 字体为Arial */
                text-align: center;
                /* 文本居中对齐 */
                margin-top: 5px;
                font-size: 40px;
                font-weight: bolder;
                z-index: 100;
            }

            #CNN_func {
                color: gray;
                font-size: 20px;
                position: absolute;
                top: 40px;
                left: 20px;
                font-style: italic;
            }

            #CNn-dropdown-box {
                color: #de77ae;
                /* 默认颜色 */
            }

            #CNN-dropdown-box:hover {
                color: #c51b7d;
                /* 鼠标悬停时的颜色 */
            }

            #CNN-dropdown-box g {
                stroke: #de77ae;
                /* 默认图形颜色 */
            }

            #CNN-dropdown-box:hover g {
                stroke: #c51b7d;
                /* 鼠标悬停时的图形颜色 */
            }

            #CNN-dropdown-deco {
                opacity: 0.5;
                /* 默认透明度 */
            }

            #CNN-dropdown-box:hover #CNN-dropdown-deco {
                opacity: 0.9;
                /* 鼠标悬停时的透明度 */
            }

            #CNN-dropdown-options-container {
                display: none;
                /* 默认不显示 */
            }

        }
    }

    #PerceptualFeaturePooling {
        position: relative;
        width: 1200px;
        height: 200px;

        // background-color: #7097c8;
        #pooling {
            border-width: 3px;
            border-style: solid;
            // border-color: #fbd28e;
            border-color: #000;

            border-radius: 5px;
            position: absolute;
            top: 100px;
            left: 606px;
            height: 98px;
            width: 350px;
            // background-color: #ffedd1;
            // background-color: #ffedd1;

            display: flex;
            /* 设置为flex布局 */
            justify-content: center;
            /* 水平居中 */
            align-items: center;

            #pooling_title {
                // color: #f49907;
                /* 文字颜色为蓝色 */
                font-family: Arial;
                /* 字体为Arial */
                text-align: center;
                /* 文本居中对齐 */
                margin-top: 5px;
                font-size: 30px;
                font-weight: bolder;
            }
        }

        #shadow {
            position: absolute;
            top: -101px;
            left: 855px;
        }
    }

    .flowing-dash {
        stroke-dasharray: 2;
        stroke-dashoffset: 0;
        animation: dash 5s linear infinite;
    }

    @keyframes dash {
        to {
            stroke-dashoffset: 30;
        }
    }

    .flowing-dash-1 {
        stroke-dasharray: 2;
        stroke-dashoffset: 30;
        animation: dash-1 5s linear infinite;
    }

    @keyframes dash-1 {
        to {
            stroke-dashoffset: 0;
        }
    }

    #GCN_group {
        position: relative;
        width: 1500px;
        height: 400px;

        .overlay-svg-2 {
            position: absolute;
            top: 0;
            left: 0;
            z-index: 10;
            /* 较高的z-index确保SVG在顶部 */
        }

        .unpooling-tags {
            color: #397200;
            /* 文字颜色为蓝色 */
            font-family: Arial;
            /* 字体为Arial */
            text-align: center;
            /* 文本居中对齐 */
            font-size: 14px;
            font-weight: bolder;
        }

        #unpooling-tag-1 {
            position: absolute;
            top: 100px;
            left: 282px;
        }

        #unpooling-tag-2 {
            position: absolute;
            top: 100px;
            left: 556px;
        }

        .vertices-tags {
            // color: #397200;
            /* 文字颜色为蓝色 */
            font-family: Arial;
            /* 字体为Arial */
            text-align: center;
            /* 文本居中对齐 */
            font-size: 25px;
            font-weight: bolder;
            z-index: 51;
        }

        #vertices-tag-1 {
            position: absolute;
            top: 200px;
            left: 82px;

        }

        #vertices-tag-2 {
            position: absolute;
            top: 200px;
            left: 358px;

        }

        #vertices-tag-3 {
            position: absolute;
            top: 200px;
            left: 632px;

        }

        #InitModel {
            position: absolute;
            top: 170px;
            left: 70px;
            z-index: 11;
        }

        #InitialModel {
            position: absolute;
            top: 150px;
            left: 70px;
            z-index: 11;
            display: inline-block;
            font-size: 35px;
            font-weight: bolder;
            width: auto;
            white-space: nowrap;
        }

        #initmodel {
            border-color: #4f900d;
            border-width: 3px;
            border-style: solid;
            border-radius: 5px;
            width: 150px;
            height: 150px;
            background-color: antiquewhite;
            position: absolute;
            top: 200px;
            left: 70px;
        }



        #GCN_part {
            position: absolute;
            top: 150px;
            background-color: #f9fdf2;
            border-width: 3px;
            border-style: solid;
            border-color: #4f900d;
            border-radius: 5px;
            width: 925px;
            height: 400px;
            left: 350px;

            #loss {
                position: absolute;
                top: 150px;
                left: 200px;

                #losscontainer {
                    position: absolute;
                    top: 170px;
                    left: 100px;
                    z-index: 11;
                }

                #charmercontainer {
                    position: absolute;
                    top: 170px;
                    left: 180px;
                    z-index: 11;
                }

                #normalcontainer {
                    position: absolute;
                    top: 170px;
                    left: 334px;
                    z-index: 11;
                }
            }

            #opti-learning {
                position: absolute;
                top: 135px;
                left: -330px;

                #optimizer {
                    position: absolute;
                    top: 170px;
                    left: 334px;
                    z-index: 11;
                }

                #learningrate {
                    position: absolute;
                    top: 190px;
                    left: 334px;
                    z-index: 11;
                }
            }

            .model {
                width: 200px;
                height: 200px;
                background-color: antiquewhite;
                position: absolute;
                top: 20px;
                z-index: 50;
            }

            #model1 {
                left: 80px;
            }

            #model2 {
                left: 355px;
            }

            #model3 {
                left: 630px;
            }

            #GCN_title {
                // color: #397200;
                /* 文字颜色为蓝色 */
                font-family: Arial;
                /* 字体为Arial */
                text-align: center;
                /* 文本居中对齐 */
                margin-top: 235px;
                font-size: 45px;
                font-weight: bolder;
            }
        }
    }


    #CNN-config {
        font-size: 20px;
        position: absolute;
        height: 50px;
        top: 200px;
        left: 70px;
        display: flex;
        align-items: center;

        #CNN-select {
            margin-left: 10px;
            width: 100px;
        }
    }

    #hidden-config {
        font-size: 20px;
        position: absolute;
        top: 250px;
        left: 40px;
        display: flex;
        align-items: center;

        #Hidden-spin {
            margin-right: 10px;
            width: 120px;
        }
    }

    #Init-config {
        font-size: 20px;
        position: absolute;
        height: 50px;
        top: 550px;
        left: 50px;
        display: flex;
        align-items: center;

        #Model-select {
            margin-left: 10px;
            width: 100px;
        }
    }

    #unpooling-config {
        font-size: 20px;
        position: absolute;
        height: 50px;
        top: 600px;
        left: 50px;
        display: flex;
        align-items: center;

        #unpooling-item {
            margin-left: 10px;
            width: 100px;
        }
    }

    #optimizer-config {
        font-size: 20px;
        position: absolute;
        height: 50px;
        top: 650px;
        left: 50px;
        display: flex;
        align-items: center;

        #optimizer-item {
            margin-left: 10px;
            width: 100px;
        }
    }

    #l_rate-config {
        font-size: 20px;
        position: absolute;
        height: 50px;
        top: 700px;
        left: 50px;
        display: flex;
        align-items: center;

        #l_rate-item {
            margin-left: 10px;
            width: 100px;
        }
    }

    #lossing-config {
        font-size: 20px;
        position: absolute;
        height: 50px;
        top: 780px;
        left: 325px;
        display: flex;
        align-items: center;

        .spin-item {
            margin-left: 10px;
            margin-right: 10px;

        }
    }

    .config-item label {
        margin-bottom: 0;
        white-space: nowrap;
    }




    // }
}
</style>