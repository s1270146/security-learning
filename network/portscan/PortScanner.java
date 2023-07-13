import java.net.Socket;

public class PortScanner {
    public static void main(String[] args) {
        String host = args[0];
        int startPort = 1;
        int endPort = 65535;

        System.out.println("ポートスキャン中...");

        for (int port = startPort; port <= endPort; port++) {
            try {
                Socket socket = new Socket(host, port);
                System.out.println("ポート " + port + " はopenです");
                socket.close();
            } catch (Exception e) {
                // System.err.println("ポート " + port + " は拒否されました");
            }
        }

        System.out.println("ポートスキャンが完了しました。");
    }
}