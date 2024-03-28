<template>
    <div class="parms-table">
        <el-table :data="tableData" :span-method="arraySpanMethod" border style="width: 100%">
            <el-table-column prop="id" label="Hyperparameters" width="150">
            </el-table-column>
            <el-table-column prop="name" label="Value" width="90">
            </el-table-column>
            <el-table-column prop="amount1" label="Status">
                <template #default="{ row }">
                    <img v-if="row.svg" :src="row.svg" alt="icon" class="icon-small" />
                    <span v-else>{{ row.amount1 }}</span>
                </template>
            </el-table-column>

        </el-table>
    </div>
</template>

<script>
import iconSvg from '/Users/daiweitao/UMG/P2MVis_SC/P2MVis_demo/src/assets/normal.svg'; // '@/assets/icon.svg' 应该是 SVG 文件的路径
import iconSvg_1 from '/Users/daiweitao/UMG/P2MVis_SC/P2MVis_demo/src/assets/cross.svg';
export default {
    data() {
        return {
            tableData: [{
                id: 'Learning Rate',
                name: '0.1',
                amount1: '',
                svg: iconSvg_1,
            }, {
                id: 'Chamfer loss',
                name: '1',
                amount1: '',
                amount2: 'Chamfer loss',
                svg: iconSvg,
            }, {
                id: 'Normal loss',
                name: '1',
                amount1: '',
                amount2: 'Normal loss',
                svg: iconSvg,
            }, {
                id: 'Regularization',
                name: '0',
                amount1: '',
                amount2: 'Regularization',
                svg: iconSvg_1,
            }, {
                id: '2D CNN',
                name: 'VGG-16',
                amount1: '',
                amount2: 'Regularization',
                svg: iconSvg,
            }, {
                id: 'Optimizer',
                name: 'Adam',
                amount1: '',
                amount2: 'Regularization',
                svg: iconSvg,
            }]
        };
    },
    methods: {
        arraySpanMethod({ row, column, rowIndex, columnIndex }) {

        },

        objectSpanMethod({ row, column, rowIndex, columnIndex }) {
            if (columnIndex === 0) {
                if (rowIndex % 2 === 0) {
                    return {
                        rowspan: 2,
                        colspan: 1
                    };
                } else {
                    return {
                        rowspan: 0,
                        colspan: 0
                    };
                }
            }
        }
    }
};
</script>

<style lang="scss" scoped>
.parms-table {
    margin: 40px 20px auto 20px
}

.icon-small {
    width: 24px;
    height: 24px;
}
</style>