import React from "react";
import TotalStudentsBySector from "./totalStudentsbySector";
import TotalStudentsByRegion from "./totalStudentsbyRegion";
import TotalStrandsByRegion from "./totalstrandsbyRegion";

const SHS: React.FC = () => {
    
    return (
        <div className="w-full flex flex-wrap">
        <div className="w-1/3">
            <TotalStudentsBySector/>
        </div>  
        {/* <div className="w-1/2">
            <TotalStudentsByRegion/>
        </div>
        <div className="w-full">
            <TotalStrandsByRegion/>
        </div> */}

        
        </div>
    );
};

export default SHS;