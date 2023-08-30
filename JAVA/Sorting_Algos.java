import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

public class SortingAlgorithmVisualizer extends JPanel {

    private static final int DATA_SIZE = 50;
    private static final int BAR_WIDTH = 10;
    private static final int BAR_SPACING = 2;
    private static final int FRAME_WIDTH = DATA_SIZE * (BAR_WIDTH + BAR_SPACING);
    private static final int FRAME_HEIGHT = 500;
    private static final int DELAY = 50;

    private int[] data;
    private SortingAlgorithm currentAlgorithm;
    private int currentIndex;

    public SortingAlgorithmVisualizer() {
        data = generateRandomData(DATA_SIZE);
        currentAlgorithm = null;
        currentIndex = 0;
        setPreferredSize(new Dimension(FRAME_WIDTH, FRAME_HEIGHT));
        setBackground(Color.BLACK);
        Timer timer = new Timer(DELAY, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (currentAlgorithm != null && currentAlgorithm.isSorting()) {
                    currentAlgorithm.step();
                    repaint();
                }
            }
        });
        timer.start();
    }

    public void visualizeSorting(SortingAlgorithm algorithm) {
        data = generateRandomData(DATA_SIZE);
        currentAlgorithm = algorithm;
        currentIndex = 0;
        currentAlgorithm.init(data);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (currentAlgorithm != null) {
            drawBars(g);
        }
    }

    private void drawBars(Graphics g) {
        for (int i = 0; i < data.length; i++) {
            int barHeight = data[i];
            int x = i * (BAR_WIDTH + BAR_SPACING);
            int y = FRAME_HEIGHT - barHeight;
            g.setColor(Color.WHITE);
            g.fillRect(x, y, BAR_WIDTH, barHeight);
        }
    }

    private int[] generateRandomData(int size) {
        int[] data = new int[size];
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            data[i] = random.nextInt(FRAME_HEIGHT - 10) + 10;
        }
        return data;
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Sorting Algorithm Visualizer");
        SortingAlgorithmVisualizer visualizer = new SortingAlgorithmVisualizer();
        frame.add(visualizer);
        frame.pack();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        String[] sortingAlgorithms = {
            "Selection Sort", "Bubble Sort", "Insertion Sort",
            "Merge Sort", "Quick Sort", "Heap Sort"
        };

        String choice = (String) JOptionPane.showInputDialog(
            frame, "Choose a sorting algorithm:", "Sorting Algorithm",
            JOptionPane.QUESTION_MESSAGE, null, sortingAlgorithms,
            sortingAlgorithms[0]);

        SortingAlgorithm algorithm = null;

        if (choice != null) {
            switch (choice) {
                case "Selection Sort":
                    algorithm = new SelectionSort();
                    break;
                case "Bubble Sort":
                    algorithm = new BubbleSort();
                    break;
                case "Insertion Sort":
                    algorithm = new InsertionSort();
                    break;
                // Add cases for Merge Sort, Quick Sort, Heap Sort
            }

            if (algorithm != null) {
                visualizer.visualizeSorting(algorithm);
            }
        }
    }
}

interface SortingAlgorithm {
    void init(int[] data);
    void step();
    boolean isSorting();
}

class SelectionSort implements SortingAlgorithm {
    private int[] data;
    private int currentMinIndex;

    @Override
    public void init(int[] data) {
        this.data = data;
        currentMinIndex = 0;
    }

    @Override
    public void step() {
        if (currentMinIndex < data.length - 1) {
            int minIndex = currentMinIndex;
            for (int j = currentMinIndex + 1; j < data.length; j++) {
                if (data[j] < data[minIndex]) {
                    minIndex = j;
                }
            }
            swap(currentMinIndex, minIndex);
            currentMinIndex++;
        }
    }

    @Override
    public boolean isSorting() {
        return currentMinIndex < data.length - 1;
    }

    private void swap(int i, int j) {
        int temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }
}

class BubbleSort implements SortingAlgorithm {
    private int[] data;
    private int currentIndex;

    @Override
    public void init(int[] data) {
        this.data = data;
        currentIndex = 0;
    }

    @Override
    public void step() {
        if (currentIndex < data.length - 1) {
            for (int j = 0; j < data.length - currentIndex - 1; j++) {
                if (data[j] > data[j + 1]) {
                    swap(j, j + 1);
                }
            }
            currentIndex++;
        }
    }

    @Override
    public boolean isSorting() {
        return currentIndex < data.length - 1;
    }

    private void swap(int i, int j) {
        int temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }
}

class InsertionSort implements SortingAlgorithm {
    private int[] data;
    private int currentIndex;

    @Override
    public void init(int[] data) {
        this.data = data;
        currentIndex = 1;
    }

    @Override
    public void step() {
        if (currentIndex < data.length) {
            int key = data[currentIndex];
            int j = currentIndex - 1;
            while (j >= 0 && data[j] > key) {
                data[j + 1] = data[j];
                j--;
            }
            data[j + 1] = key;
            currentIndex++;
        }
    }

    @Override
    public boolean isSorting() {
        return currentIndex < data.length;
    }
}

// Implement Merge Sort, Quick Sort, and Heap Sort similarly

