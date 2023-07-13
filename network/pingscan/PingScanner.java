import java.io.IOException;

public class PingScanner {
    public static void main(String[] args) {
        String subnet = "172.18.0";
        int timeout = 1000;

        System.out.println("Pingスキャンを開始...");

        for (int i = 1; i <= 255; i++){
            String host = subnet + "." + i;

            try {
                Process process = Runtime.getRuntime().exec("ping -c 1 -W " + timeout + " " + host);
                int exitCode = process.waitFor();

                if (exitCode == 0) {
                    System.out.println("ホスト " + host + " は応答しています。");
                }
            } catch (IOException | InterruptedException e) {
                System.err.println("ホスト " + host + " のpingに失敗しました。 : " + e.getMessage());
            }
        }
        System.out.println("Pingスキャンが完了しました。");
    }
}