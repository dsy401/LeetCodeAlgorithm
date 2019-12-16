const validIPAddress  = (IP) =>{
    if (IP.split('.').length === 4){
        const IPList = IP.split('.')
        for (let i=0;i<IPList.length;i++){
            if (Number(IPList[i])>=256 || Number(IPList[i])<0|| Number(IPList[i]).toString() !==IPList[i]) return "Neither"
        }
        return 'IPv4'
    }else{
       if (IP.split(':').length === 8){
           const IPList = IP.split(':');
           for (let i=0;i<IPList.length;i++){
               if (IPList[i]==='' || IPList[i].length>4) return "Neither"
               for (let j=0;j<IPList[i].length;j++){
                   if (!/[a-f]|[0-9]|[A-F]/.test(IPList[i][j])) return "Neither"
               }
           }
           return 'IPv6'
       }else{
           return 'Neither'
       }
    }
};
