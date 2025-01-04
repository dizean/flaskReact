import React, { useEffect, useState } from "react";

const TotalStudentsByRegion: React.FC = () => {
    const [result, setResult] = useState<{years: number; plotHTML: string } | null>(null);
    const [currentYearIndex, setCurrentYearIndex] = useState(0);
    const [plotHtmlUrl, setPlotHtmlUrl] = useState<string | null>(null);
    const [loadingData, setLoadingData] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://localhost:5000/totalStudentsbyRegion");
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const data = await response.json();
                setResult(data);
                console.log(data)
                if (data.plotHTML) {
                    setPlotHtmlUrl(data.plotHTML);
                }
            } catch (error) {
                console.error("Error fetching data:", error);
            } finally {
                setLoadingData(false);
            }
        };
        fetchData();
    }, []);

    const updatePlotIndices = async ( newYearIndex: number) => {
        try {
            const response = await fetch("http://localhost:5000/totalStudentsbyRegion", {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({  yearIndex: newYearIndex }),
            });
            if (response.ok) {
                const updatedData = await response.json();
                console.log("Updated Data:", updatedData);
                if (updatedData.updatedPlot) {
                    setPlotHtmlUrl(updatedData.updatedPlot);
                } else {
                    console.error("No plotHTML returned from server.");
                }
            } else {
                console.error("Error updating plot:", response.statusText);
            }
        } catch (error) {
            console.error("Error updating plot:", error);
        }
    };

    const buttonNextYear = () => {
        if (result) {
            const newYearIndex = Math.min(currentYearIndex + 1, result.years - 1);
            setCurrentYearIndex(newYearIndex);
            updatePlotIndices(newYearIndex);
        }
    };

    const buttonPreviousYear = () => {
        if (result) {
            const newYearIndex = Math.max(currentYearIndex - 1, 0);
            setCurrentYearIndex(newYearIndex);
            updatePlotIndices(newYearIndex);
        }
    };

    return (
        <div className="p-6 bg-gray-100 rounded-lg shadow-md">
            <h1 className="text-3xl font-bold text-center mb-4">Total Students All Regions</h1>
            {loadingData ? (
                <p className="text-lg text-gray-600 text-center">Loading data...</p>
            ) : result ? (
                <div className="bg-red-300">
                    <div className="flex justify-center space-x-4 mb-6">
                        <button onClick={buttonPreviousYear} disabled={currentYearIndex === 0} className={`px-4 py-2 font-semibold text-white bg-purple-500 rounded-lg hover:bg-purple-600 focus:outline-none focus:ring focus:ring-purple-300 ${currentYearIndex === 0 ? 'opacity-50 cursor-not-allowed' : ''}`}>
                            Previous Year
                        </button>
                        <button onClick={buttonNextYear} disabled={currentYearIndex >= result.years - 1} className={`px-4 py-2 font-semibold text-white bg-purple-500 rounded-lg hover:bg-purple-600 focus:outline-none focus:ring focus:ring-purple-300 ${currentYearIndex >= result.years - 1 ? 'opacity-50 cursor-not-allowed' : ''}`}>
                            Next Year
                        </button>
                    </div>
                    {plotHtmlUrl ? (
                        <iframe srcDoc={plotHtmlUrl} title="External HTML Content" className="w-full h-[500px] border-none rounded-lg shadow-md" />
                    ) : (
                        <p className="text-lg text-gray-600 text-center">No plot available.</p>
                    )}
                </div>
            ) : (
                <p className="text-lg text-red-600 text-center">Error loading data.</p>
            )}
        </div>
    );
};

export default TotalStudentsByRegion;