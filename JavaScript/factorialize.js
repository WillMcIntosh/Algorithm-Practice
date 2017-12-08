function factorialize(num) {
    // in case of 0
    if (num === 0) {
        return 1;
    }else{

        // used a recursive function
        // https://www.youtube.com/watch?v=Mv9NEXX1VHc
        return num * factorialize(num - 1);

    }
}

factorialize(5);
