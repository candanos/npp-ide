public static void main(String[] args) {
	System.out.println("main started.");
	if(args.length > 0) {
        for(String arg: args) {
            System.out.println(arg)
        }
    } else {
        System.out.println("No arguments passed!");
    }
    
    
    try {
        Scanner contents = new Scanner(new File(playerFile));
        return Integer.parseInt(contents.nextLine());
    } catch (FileNotFoundException noFile) {
        throw new IllegalArgumentException("File not found");
    } finally {
        if (contents != null) {
            contents.close();
        }
    }
    // int[] inputArr = { 55, 45, 33, 22, 11 };
	// int[] sortedArr = bubbleSort(inputArr);

}