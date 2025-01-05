import React, { useEffect, useState } from "react";
import Plot from "react-plotly.js";

interface GraphData {
    data: any[];
    layout: any;
    config: any;
}
const SHSDASHBOARD: React.FC = () =>{
    const [graphData, setGraphData] = useState<{ [key: string]: GraphData } | null>(null);
        const [data, setData] = useState({
            overall : 0,
            male : 0,
            female: 0,
            gr11 : 0,
            gr12 : 0,
            private : 0,
            suclucs : 0,
            public : 0
        })
        useEffect(() => {
            fetch('http://localhost:5000/allgraphs')
                .then((response) => response.json())
                .then((data) => {
                    setData({
                        overall: data.data['Grand Total of All Students'],
                        male: data.data['Grand Total Male Students'],
                        female: data.data['Grand Total Female Students'],
                        gr11: data.data['Grade 11 Total Students'],
                        gr12: data.data['Grade 12 Total Students'],
                        private: data.sector[0]['Total Students'],
                        public: data.sector[1]['Total Students'],
                        suclucs : data.sector[2]['Total Students']
                    });
                    setGraphData(data);
                    console.log(data)
                })
                .catch((error) => {
                    console.error('Error fetching plot data:', error);
                });
        }, []);
    
        if (!graphData) {
            return <div>Loading...</div>;
        }
    return(
        <div className="w-full h-full p-10">
        {/*  */}
        <div className="w-full flex flex-wrap ">
        <div className="w-3/5  flex flex-wrap rounded-lg border-2 shadow-lg p-2 "> 
        <h1 className="text-3xl p-5 text-left">Overall students by region and year</h1>
            <Plot
            data={graphData.region.data}
            layout={graphData.region.layout}
            config={graphData.region.config}
            />
        </div>
        <div className="w-2/5  flex flex-wrap rounded-lg border-2 shadow-lg p-2 ">
        <h1 className="text-3xl p-5 text-left">Overall students</h1>
            <Plot
            data={graphData.graph_11_12.data}
            layout={graphData.graph_11_12.layout}
            config={graphData.graph_11_12.config}
            />
        </div>
        </div>
        {/*  */}
        <div className="w-full flex flex-wrap justify-evenly p-4">
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">Overall Students</h2>
            <p className="text-3xl font-bold text-center">{data.overall.toLocaleString()}</p>
        </div>
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">Overall Male Students</h2>
            <p className="text-3xl font-bold text-center">{data.male.toLocaleString()}</p>
        </div>
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">Overall Female Students</h2>
            <p className="text-3xl font-bold text-center">{data.female.toLocaleString()}</p>
        </div>
        </div>
        {/*  */}
        <div className="w-full flex flex-wrap ">
        <div className="w-2/5  flex flex-wrap  rounded-lg border-2 shadow-lg p-2 ">
            <h1 className="text-3xl p-5 text-left">Overall students in each strand</h1>
            <Plot
            data={graphData.strand.data}
            layout={graphData.strand.layout}
            config={graphData.strand.config}
            />
        </div>
        <div className="w-3/5 flex flex-wrap  rounded-lg border-2 shadow-lg p-2"> 
            <h1 className="text-3xl p-5 text-left">Overall Student by Gender in each strand</h1>
            <Plot
            data={graphData.grouped.data}
            layout={graphData.grouped.layout}
            config={graphData.grouped.config}
            />
        </div>
        </div>
        {/*  */}
        <div className="w-full flex flex-wrap justify-evenly p-4">
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">Overall Grade 11 Students</h2>
            <p className="text-3xl font-bold text-center">{data.gr11.toLocaleString()}</p>
        </div>
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">Overall Grade 12 Students</h2>
            <p className="text-3xl font-bold text-center">{data.gr12.toLocaleString()}</p>
        </div>
        </div>
        {/*  */}
        <div className="w-full flex flex-wrap ">
        <div className="w-1/2  flex flex-wrap rounded-lg border-2 shadow-lg p-2">
            <h1 className="text-3xl p-5 text-left">Grade 11 Students by Gender</h1>
             <Plot
                data={graphData.graph_11_male_female.data}
                layout={graphData.graph_11_male_female.layout}
                config={graphData.graph_11_male_female.config}
            />
        </div>
        <div className="w-1/2 flex flex-wrap rounded-lg border-2 shadow-lg p-2"> 
            <h1 className="text-3xl p-5 text-left">Grade 12 Students by Gender</h1>
            <Plot
                data={graphData.graph_12_male_female.data}
                layout={graphData.graph_12_male_female.layout}
                config={graphData.graph_12_male_female.config}
            />
        </div>
        </div>
        {/*  */}
        {/*  */}
        <div className="w-full flex flex-wrap justify-evenly p-4">
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">Public Sector</h2>
            <p className="text-3xl font-bold text-center">{data.public.toLocaleString()}</p>
        </div>
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">Private Sector</h2>
            <p className="text-3xl font-bold text-center">{data.private.toLocaleString()}</p>
        </div>
        <div className="w-full sm:w-1/5  p-4 flex flex-col justify-center rounded-lg shadow-lg">
            <h2 className="text-xl font-semibold mb-2">SucLucs Sector</h2>
            <p className="text-3xl font-bold text-center">{data.suclucs.toLocaleString()}</p>
        </div>
        </div>
        {/*  */}
        <div className="w-full flex flex-wrap ">
        <div className="w-full  flex flex-wrap rounded-lg border-2 shadow-lg p-2">
            <h1 className="text-3xl p-5 text-left">Overall Students in each Sector by Year</h1>
             <Plot
                data={graphData.sectorchart.data}
                layout={graphData.sectorchart.layout}
                config={graphData.sectorchart.config}
            />
        </div>
        </div>
        </div>
    )
}

export default SHSDASHBOARD