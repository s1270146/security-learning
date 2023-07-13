import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;

/**
 * IdleScan
 */
public class IdleScan {
    public static void main(String[] args) {
        String targetIP = args[0];
        int targetPort = Integer.parseInt(args[1]);
        int zombiePort = Integer.parseInt(args[2]);

        try {
            Socket zombiSocket = new Socket(targetIP, zombiePort);

            Socket localSocket = new Socket(InetAddress.getLocalHost(), targetPort);

            if(isPortOpen(localSocket)){
                System.out.println("ポート " + targetPort + " は開いています");
            } else {
                System.out.println("ポート " + targetPort + " は閉じています");
            }
            zombiSocket.close();
            localSocket.close();
        } catch (IOException e) {
            System.err.println("エラー : " + e.getMessage());
        }
    }

    private static boolean isPortOpen(Socket socket) {
        try {
            socket.setSoTimeout(5000);
            return (socket.getInputStream().read() == -1);
        } catch (Exception e) {
            return false;
        }
    }
}