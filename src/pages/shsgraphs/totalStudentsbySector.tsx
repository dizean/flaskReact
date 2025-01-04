import React, { useEffect, useState } from "react";

const TotalStudentsBySector: React.FC = () => {
    const [result, setResult] = useState<{ regions: number; genders: number; years: number; plotHTML: string } | null>(null);
    const [currentRegionIndex, setCurrentRegionIndex] = useState(0);
    const [currentGenderIndex, setCurrentGenderIndex] = useState(0);
    const [currentYearIndex, setCurrentYearIndex] = useState(0);
    const [plotHtmlUrl, setPlotHtmlUrl] = useState<string | null>(null);
    const [loadingData, setLoadingData] = useState(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://localhost:5000/totalStudentsbySector");
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

    const updatePlotIndices = async (newRegIndex: number, newGenIndex: number, newYearIndex: number) => {
        try {
            const response = await fetch("http://localhost:5000/totalStudentsbySector", {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ regIndex: newRegIndex, genIndex: newGenIndex, yearIndex: newYearIndex }),
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

    const buttonNextRegion = () => {
        if (result) {
            const newRegionIndex = Math.min(currentRegionIndex + 1, result.regions - 1);
            setCurrentRegionIndex(newRegionIndex);
            updatePlotIndices(newRegionIndex, currentGenderIndex, currentYearIndex);
        }
    };

    const buttonPreviousRegion = () => {
        if (result) {
            const newRegionIndex = Math.max(currentRegionIndex - 1, 0);
            setCurrentRegionIndex(newRegionIndex);
            updatePlotIndices(newRegionIndex, currentGenderIndex, currentYearIndex);
        }
    };

    const buttonNextGender = () => {
        if (result) {
            const newGenderIndex = Math.min(currentGenderIndex + 1, result.genders - 1);
            setCurrentGenderIndex(newGenderIndex);
            updatePlotIndices(currentRegionIndex, newGenderIndex, currentYearIndex);
        }
    };

    const buttonPreviousGender = () => {
        if (result) {
            const newGenderIndex = Math.max(currentGenderIndex - 1, 0);
            setCurrentGenderIndex(newGenderIndex);
            updatePlotIndices(currentRegionIndex, newGenderIndex, currentYearIndex);
        }
    };

    const buttonNextYear = () => {
        if (result) {
            const newYearIndex = Math.min(currentYearIndex + 1, result.years - 1);
            setCurrentYearIndex(newYearIndex);
            updatePlotIndices(currentRegionIndex, currentGenderIndex, newYearIndex);
        }
    };

    const buttonPreviousYear = () => {
        if (result) {
            const newYearIndex = Math.max(currentYearIndex - 1, 0);
            setCurrentYearIndex(newYearIndex);
            updatePlotIndices(currentRegionIndex, currentGenderIndex, newYearIndex);
        }
    };

    return (
        <div className="p-6 bg-gray-100 rounded-lg shadow-md">
            <h1 className="text-3xl font-bold text-center mb-4">Total Students by Sector</h1>
            {loadingData ? (
                <p className="text-lg text-gray-600 text-center">Loading data...</p>
            ) : result ? (
                <div>
                    <div className="flex justify-center space-x-4 mb-4">
                        <button onClick={buttonPreviousRegion} disabled={currentRegionIndex === 0} className={`px-4 py-2 font-semibold text-white bg-green-500 rounded-lg hover:bg-green-600 focus:outline-none focus:ring focus:ring-green-300 ${currentRegionIndex === 0 ? 'opacity-50 cursor-not-allowed' : ''}`}>
                            Previous Region
                        </button>
                        <button onClick={buttonNextRegion} disabled={currentRegionIndex >= result.regions - 1} className={`px-4 py-2 font-semibold text-white bg-green-500 rounded-lg hover:bg-green-600 focus:outline-none focus:ring focus:ring-green-300 ${currentRegionIndex >= result.regions - 1 ? 'opacity-50 cursor-not-allowed' : ''}`}>
                            Next Region
                        </button>
                    </div>
                    <div className="flex justify-center space-x-4 mb-4">
                        <button onClick={buttonPreviousGender} disabled={currentGenderIndex === 0} className={`px-4 py-2 font-semibold text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 ${currentGenderIndex === 0 ? 'opacity-50 cursor-not-allowed' : ''}`}>
                            Previous Gender
                        </button>
                        <button onClick={buttonNextGender} disabled={currentGenderIndex >= result.genders - 1} className={`px-4 py-2 font-semibold text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 ${currentGenderIndex >= result.genders - 1 ? 'opacity-50 cursor-not-allowed' : ''}`}>
                            Next Gender
                        </button>
                    </div>
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

export default TotalStudentsBySector;