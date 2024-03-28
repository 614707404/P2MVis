<template>
  <div class="chart-container">
    <div class="legend">
      <div v-for="(dataset, index) in datasets" :key="index" class="legend-item" @click="toggleDataset(index)">
        <div :style="{ background: colors[index] }" class="color-box"></div>
        <div>{{ dataset.name }}</div>
      </div>
    </div>
    <svg ref="svg" :width="width" :height="height"></svg>
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "LineChart",
  props: {
    width: {
      type: Number,
      default: 1350
    },
    height: {
      type: Number,
      default: 150
    },
    datasets: {
      type: Array,
      required: true
    },
    xData: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      colors: d3.schemeCategory10,
      visibleDatasets: this.datasets.map(() => true), // 初始时，所有数据集都是可见的
    };
  },
  watch: {
    datasets: {
      handler() {
        this.drawChart();
      },
      deep: true
    }
  },
  mounted() {
    this.drawChart();
  },
  methods: {
    toggleDataset(index) {
      // 切换对应数据集的显示状态
      this.visibleDatasets[index] = !this.visibleDatasets[index];
      // 重新绘制图表以反映更改
      this.drawChart();
    },
    drawChart() {
      const svg = d3.select(this.$refs.svg);
      svg.selectAll("*").remove();

      // const yMax = d3.max(this.datasets, d => Math.ceil(d3.max(d.data))) > 0 ? d3.max(this.datasets, d => Math.ceil(d3.max(d.data))) : 5;
      const yMax = d3.max(this.datasets.filter((_, i) => this.visibleDatasets[i]), dataset =>
        d3.max(dataset.data)
      ) || 0.1; // 如果没有可见数据，使用默认值5
      const xMax = this.xData.length > 0 ? this.xData.length - 1 : 10;

      const xScale = d3.scaleLinear().domain([0, xMax]).range([10, this.width - 10]);
      const yScale = d3.scaleLinear().domain([0, yMax]).range([this.height - 10, 10]).nice();

      const xAxis = d3.axisBottom(xScale).ticks(10).tickFormat((d, i) => this.xData[i]);
      const yAxis = d3.axisLeft(yScale).tickFormat(d3.format("d"));
      //      const xAxis = d3.axisBottom(xScale).tickValues([xMin, (xMin + xMax) / 2, xMax]);
      // const yAxis = d3.axisLeft(yScale).tickValues([yMin, (yMin + yMax) / 2, yMax]);

      // 创建x轴作为网格
      const xAxisGrid = d3.axisBottom(xScale).tickSize(-this.height + 20).tickFormat('').ticks(15);
      // 创建y轴作为网格
      const yAxisGrid = d3.axisLeft(yScale).tickSize(-this.width + 20).tickFormat('').ticks(10);
      // 绘制x轴网格
      svg.append("g")
        .attr("class", "grid")
        .attr("transform", `translate(0,${this.height - 10})`)
        .call(xAxisGrid)
        .selectAll("line") // 选择所有线
        .style("stroke", "gray") // 设置线的颜色
        .style("stroke-opacity", 0.5) // 设置线的透明度
        .style("shape-rendering", "crispEdges");
      // 绘制y轴网格
      svg.append("g")
        .attr("class", "grid")
        .attr("transform", "translate(10,0)")
        .call(yAxisGrid)
        .selectAll("line") // 同样选择所有线
        .style("stroke", "gray") // 设置线的颜色
        .style("stroke-opacity", 0.5) // 设置线的透明度
        .style("shape-rendering", "crispEdges");

      svg.append("g").attr("transform", `translate(0,${this.height - 10})`).call(xAxis);
      svg.append("g").attr("transform", "translate(10,0)").call(yAxis);

      if (this.xData.length > 0) {
        this.datasets.forEach((dataset, index) => {
          if (this.visibleDatasets[index]) {
            const line = d3.line()
              .x((d, i) => xScale(i))
              .y(d => yScale(d));

            svg.append("path")
              .attr("fill", "none")
              .attr("stroke", this.colors[index])
              .attr("stroke-width", 2)
              .attr("d", line(dataset.data));
          }
        });
      }
    }

  }
};

</script>

<style scoped>
.chart-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  /* 占满父组件的宽度 */
  height: 100%;
  /* 占满父组件的高度 */
}

.legend {
  display: flex;
  flex-direction: row;
  /* Change from column to row for horizontal layout */
  flex-wrap: wrap;
  /* Allows legend items to wrap onto the next line if space is limited */


}

.legend-item {
  display: flex;
  align-items: center;
  margin-left: 10px;
  /* Add space between legend items */
}

.color-box {
  width: 10px;
  height: 10px;
  margin-right: 5px;
}
</style>
