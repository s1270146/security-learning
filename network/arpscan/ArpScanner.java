import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ArpScanner {
    public static void main(String[] args) {
        String subnet = "172.18.0"; // スキャンするサブネット

        System.out.println("ARPスキャンを開始します...");

        for (int i = 1; i <= 255; i++) {
            String host = subnet + "." + i;

            try {
                Process process = Runtime.getRuntime().exec("arp -a " + host);
                BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                String line;

                while ((line = reader.readLine()) != null) {
                    if (line.toLowerCase().contains(host.toLowerCase())) {
                        System.out.println("ホスト " + host + " は存在します");
                        break;
                    }
                }

                reader.close();
            } catch (IOException e) {
                // エラーメッセージを表示
                System.err.println("ホスト " + host + " のARPスキャンに失敗しました: " + e.getMessage());
            }
        }

        System.out.println("ARPスキャンが完了しました。");
    }
}
