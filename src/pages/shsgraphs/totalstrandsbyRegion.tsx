import React, { useEffect, useState } from "react";

const TotalStrandsByRegion: React.FC = () => {
    const [result, setResult] = useState<{ regions: number; sectors: number; gradeGender: number; plotHTML: string } | null>(null);
    const [currentSectorIndex, setCurrentSectorIndex] = useState(0);
    const [currentRegionIndex, setCurrentRegionIndex] = useState(0);
    const [currentGradeGenderIndex, setCurrentGradeGenderIndex] = useState(0);
    const [plotHtmlUrl, setPlotHtmlUrl] = useState<string | null>(null);
    const [loadingData, setLoadingData] = useState(true); 
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://localhost:5000/totalbyStrandEachRegion");
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                const data = await response.json();
                setResult(data);
                
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
    const updatePlotIndices = async (newRegIndex: number, newSecIndex: number, newGradeGenIndex: number) => {
        try {
            const response = await fetch("http://localhost:5000/totalbyStrandEachRegion", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    regIndex: newRegIndex,
                    secIndex: newSecIndex,
                    gradegenIndex: newGradeGenIndex
                }),
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

    const buttonNextSector = () => {
        if (result) {
            const newSectorIndex = Math.min(currentSectorIndex + 1, result.sectors - 1);
            setCurrentSectorIndex(newSectorIndex);
            updatePlotIndices(currentRegionIndex, newSectorIndex, currentGradeGenderIndex);
        }
    };

    const buttonPreviousSector = () => {
        if (result) {
            const newSectorIndex = Math.max(currentSectorIndex - 1, 0);
            setCurrentSectorIndex(newSectorIndex);
            updatePlotIndices(currentRegionIndex, newSectorIndex, currentGradeGenderIndex);
        }
    };

    const buttonNextRegion = () => {
        if (result) {
            const newRegionIndex = Math.min(currentRegionIndex + 1, result.regions - 1);
            setCurrentRegionIndex(newRegionIndex);
            updatePlotIndices(newRegionIndex, currentSectorIndex, currentGradeGenderIndex);
        }
    };

    const buttonPreviousRegion = () => {
        if (result) {
            const newRegionIndex = Math.max(currentRegionIndex - 1, 0);
            setCurrentRegionIndex(newRegionIndex);
            updatePlotIndices(newRegionIndex, currentSectorIndex, currentGradeGenderIndex);
        }
    };

    const buttonNextGradeGender = () => {
        if (result) {
            const newGradeGenderIndex = Math.min(currentGradeGenderIndex + 1, result.gradeGender - 1);
            setCurrentGradeGenderIndex(newGradeGenderIndex);
            updatePlotIndices(currentRegionIndex, currentSectorIndex, newGradeGenderIndex);
        }
    };

    const buttonPreviousGradeGender = () => {
        if (result) {
            const newGradeGenderIndex = Math.max(currentGradeGenderIndex - 1, 0);
            setCurrentGradeGenderIndex(newGradeGenderIndex);
            updatePlotIndices(currentRegionIndex, currentSectorIndex, newGradeGenderIndex);
        }
    };

    return (
        <div className="p-6 bg-gray-100 rounded-lg shadow-md">
        <h1 className="text-3xl font-bold text-center mb-4">Total Students of Each Strands By Region</h1>
        {loadingData ? (
            <p className="text-lg text-gray-600 text-center">Loading data...</p>
        ) : result ? (
            <div>
                <div className="flex justify-center space-x-4 mb-4">
                    <button 
                        onClick={buttonPreviousSector} 
                        disabled={currentSectorIndex === 0 && (currentGradeGenderIndex >= 15 && currentGradeGenderIndex <= 21)}
                        className={`px-4 py-2 font-semibold text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 ${currentSectorIndex === 0 ? 'opacity-50 cursor-not-allowed' : ''}`}
                    >
                        Previous Sector
                    </button>
                    <button 
                        onClick={buttonNextSector} 
                        disabled={currentSectorIndex >= result.sectors - 1 && (currentGradeGenderIndex >= 15 && currentGradeGenderIndex <= 21)}
                        className={`px-4 py-2 font-semibold text-white bg-blue-500 rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 ${currentSectorIndex >= result.sectors - 1 ? 'opacity-50 cursor-not-allowed' : ''}`}
                    >
                        Next Sector
                    </button>
                </div>
    
                <div className="flex justify-center space-x-4 mb-4">
                    <button 
                        onClick={buttonPreviousRegion} 
                        disabled={currentRegionIndex === 0}
                        className={`px-4 py-2 font-semibold text-white bg-green-500 rounded-lg hover:bg-green-600 focus:outline-none focus:ring focus:ring-green-300 ${currentRegionIndex === 0 ? 'opacity-50 cursor-not-allowed' : ''}`}
                    >
                        Previous Region
                    </button>
                    <button 
                        onClick={buttonNextRegion} 
                        disabled={currentRegionIndex >= result.regions - 1}
                        className={`px-4 py-2 font-semibold text-white bg-green-500 rounded-lg hover:bg-green-600 focus:outline-none focus:ring focus:ring-green-300 ${currentRegionIndex >= result.regions - 1 ? 'opacity-50 cursor-not-allowed' : ''}`}
                    >
                        Next Region
                    </button>
                </div>
    
                <div className="flex justify-center space-x-4 mb-6">
                    <button 
                        onClick={buttonPreviousGradeGender} 
                        disabled={currentGradeGenderIndex === 0}
                        className={`px-4 py-2 font-semibold text-white bg-purple-500 rounded-lg hover:bg-purple-600 focus:outline-none focus:ring focus:ring-purple-300 ${currentGradeGenderIndex === 0 ? 'opacity-50 cursor-not-allowed' : ''}`}
                    >
                        Previous Grade/Gender
                    </button>
                    <button 
                        onClick={buttonNextGradeGender} 
                        disabled={currentGradeGenderIndex >= result.gradeGender - 1}
                        className={`px-4 py-2 font-semibold text-white bg-purple-500 rounded-lg hover:bg-purple-600 focus:outline-none focus:ring focus:ring-purple-300 ${currentGradeGenderIndex >= result.gradeGender - 1 ? 'opacity-50 cursor-not-allowed' : ''}`}
                    >
                        Next Grade/Gender
                    </button>
                </div>
                {plotHtmlUrl ? (
                     <iframe srcDoc={plotHtmlUrl} title="External HTML Content" className="w-full h-[500px] border-none rounded-lg shadow-md bg-emerald-300" />
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

export default TotalStrandsByRegion;